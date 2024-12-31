from datetime import datetime
from django.utils import timezone
from django.db.models import Sum
from accounts.operations.operations_bankcharges.models import BankCharges
from accounts.operations.operations_paymentvouchers.models import PaymentVoucher
from accounts.operations.operations_pettycash.models import PettyCash
from accounts.operations.operations_receipts.models import OperationReceipt
from accounts.operations.operations_balances.utils import calculate_balance_carried_forward

def get_payments_money_out(year, month):
    payments = []
    total_cash_payments = 0
    total_bank_payments = 0
    total_bankcharges = 0

    start_date = timezone.make_aware(datetime(year, month, 1))
    end_date = timezone.make_aware(datetime(year, month + 1, 1)) if month < 12 else timezone.make_aware(datetime(year + 1, 1, 1))

    # Fetch Bank Charges within the specified month and year
    bank_charges = BankCharges.objects.filter(charge_date__gte=start_date, charge_date__lt=end_date)
    for charge in bank_charges:
        total_bankcharges += charge.amount
        payments.append({
            "type": "bankcharge",
            "voucher_no": "",
            "cheque_no": "",
            "cash": "",
            "bank": "",
            "bank_charge": charge.amount,
            "description": charge.description,
            "date": charge.charge_date
        })

    # Fetch Payment Vouchers within the specified month and year
    payment_vouchers = PaymentVoucher.objects.filter(date__gte=start_date, date__lt=end_date)
    for voucher in payment_vouchers:
        if voucher.payment_mode == 'cash':
            total_cash_payments += voucher.amount_shs
        elif voucher.payment_mode == 'bank':
            total_bank_payments += voucher.amount_shs
        payments.append({
            "type": "paymentvoucher",
            "voucher_no": voucher.voucher_no,
            "cheque_no": voucher.cheque_number if voucher.payment_mode == 'bank' else "",
            "cash": voucher.amount_shs if voucher.payment_mode == 'cash' else "",
            "bank": voucher.amount_shs if voucher.payment_mode == 'bank' else "",
            "bank_charge": "",
            "description": voucher.particulars,
            "date": voucher.date
        })

    # Fetch Petty Cash Entries within the specified month and year
    petty_cash_entries = PettyCash.objects.filter(date_issued__gte=start_date, date_issued__lt=end_date)
    for petty_cash in petty_cash_entries:
        total_cash_payments += petty_cash.amount  # Add Petty Cash amount to total cash payments
        payments.append({
            "type": "pettycash",
            "voucher_no": "",
            "cheque_no": petty_cash.cheque_number,
            "cash": petty_cash.amount,
            "bank": "",
            "bank_charge": "",
            "description": petty_cash.description,
            "date": petty_cash.date_issued
        })

    total_payments = {
        "total_cash_payments": total_cash_payments,
        "total_bank_payments": total_bank_payments,
        "total_bankcharges": total_bankcharges
    }

    return {"payments": payments, "total_payments": total_payments}

def get_receipts_money_in(year, month):
    balance_info = calculate_balance_carried_forward(year, month)

    receipts_data = []
    total_cash_received = 0
    total_bank_received = 0

    balance_forward = {
        'from_whom': 'Balance Carried Forward',
        'receipt_no': '-',
        'cash': f"{balance_info['cashAmount']:,}" if balance_info['cashAmount'] is not None else '-',
        'bank': f"{balance_info['bankAmount']:,}" if balance_info['bankAmount'] is not None else '-',
        'rmi': '-',
        'other_voteheads': '-',
    }
    receipts_data.append(balance_forward)

    start_date = timezone.make_aware(datetime(year, month, 1))
    end_date = timezone.make_aware(datetime(year, month + 1, 1)) if month < 12 else timezone.make_aware(datetime(year + 1, 1, 1))

    # Petty Cash Receipts
    petty_cash_entries = OperationReceipt.objects.filter(
        received_from='pettycash',
        date__gte=start_date,
        date__lt=end_date
    ).values('petty_cash__payee_name').annotate(
        total_amount=Sum('total_amount')
    )

    for entry in petty_cash_entries:
        total_amount = entry['total_amount'] or 0
        total_cash_received += total_amount
        receipts_data.append({
            'from_whom': 'Petty Cash',
            'receipt_no': '-',
            'cash': f"{total_amount:,}",
            'bank': '-',
            'rmi': '-',
            'other_voteheads': '-',
            'date': start_date  # Add a default date if none is available
        })

    # Operation Receipts (non-petty cash)
    operation_receipts = OperationReceipt.objects.exclude(
        received_from='pettycash'
    ).filter(
        date__gte=start_date,
        date__lt=end_date
    ).values(
        'received_from', 'cash_bank', 'total_amount', 'rmi_fund', 'other_voteheads', 'date'
    )

    for receipt in operation_receipts:
        total_amount = receipt['total_amount'] or 0
        rmi_fund = receipt['rmi_fund'] or 0
        other_voteheads = receipt['other_voteheads'] or 0
        receipt_date = receipt.get('date', start_date)  # Default to start_date if no date is provided

        if receipt['cash_bank'] == 'cash':
            total_cash_received += total_amount
        elif receipt['cash_bank'] == 'bank':
            total_bank_received += total_amount

        receipts_data.append({
            'from_whom': receipt['received_from'],
            'receipt_no': '-',
            'cash': f"{total_amount:,}" if receipt['cash_bank'] == 'cash' else '-',
            'bank': f"{total_amount:,}" if receipt['cash_bank'] == 'bank' else '-',
            'rmi': f"{rmi_fund:,}" if rmi_fund > 0 else '-',
            'other_voteheads': f"{other_voteheads:,}" if other_voteheads > 0 else '-',
            'date': receipt_date  # Ensure the date is added
        })

    total_receipts = {
        "total_cash_received": total_cash_received,
        "total_bank_received": total_bank_received
    }

    return {"receipts": receipts_data, "total_receipts": total_receipts}




def get_cashbook(year, month):
    cashbook_data = {
        "receipts": [],
        "payments": []
    }

    # Get Receipts (Money In)
    receipts = get_receipts_money_in(year, month)
    cashbook_data["receipts"].extend(receipts["receipts"])

    # Get Payments (Money Out)
    payments = get_payments_money_out(year, month)
    cashbook_data["payments"].extend(payments["payments"])

    # Add total_receipts and total_payments
    cashbook_data["total_receipts"] = receipts["total_receipts"]
    cashbook_data["total_payments"] = payments["total_payments"]

    return cashbook_data
