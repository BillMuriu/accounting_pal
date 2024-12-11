from datetime import datetime
from django.utils import timezone
from django.db.models import Sum
from accounts.rmi.rmi_bankcharges.models import RMIBankCharge
from accounts.rmi.rmi_paymentvoucher.models import RMIPaymentVoucher
from accounts.rmi.rmi_pettycash.models import RMIPettyCash
from accounts.rmi.rmi_receipts.models import RMIReceipt
from accounts.rmi.rmi_balances.utils import calculate_rmi_balance_carried_forward

def get_rmi_payments_money_out(year, month):
    payments = []

    # Define the start and end date for the specified month and year
    start_date = timezone.make_aware(datetime(year, month, 1))
    end_date = timezone.make_aware(datetime(year + 1, 1, 1)) if month == 12 else timezone.make_aware(datetime(year, month + 1, 1))

    # Fetch Bank Charges within the specified month and year
    bank_charges = RMIBankCharge.objects.filter(charge_date__gte=start_date, charge_date__lte=end_date)
    for charge in bank_charges:
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
    payment_vouchers = RMIPaymentVoucher.objects.filter(date__gte=start_date, date__lt=end_date)
    for voucher in payment_vouchers:
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
    petty_cash_entries = RMIPettyCash.objects.filter(date_issued__gte=start_date, date_issued__lt=end_date)
    for petty_cash in petty_cash_entries:
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

    return {"payments": payments}

def get_rmi_receipts_money_in(year, month):
    # Get the balance carried forward for the specified year and month
    balance_info = calculate_rmi_balance_carried_forward(year, month)

    # Initialize the data structure with the balance carried forward
    receipts_data = []

    balance_forward = {
        'from_whom': 'Balance Carried Forward',
        'receipt_no': '-',
        'cash': f"{balance_info['cashAmount']:,}",
        'bank': f"{balance_info['bankAmount']:,}",
    }
    receipts_data.append(balance_forward)

    # Define the start and end date for the specified month and year
    start_date = timezone.make_aware(datetime(year, month, 1))
    end_date = timezone.make_aware(datetime(year + 1, 1, 1)) if month == 12 else timezone.make_aware(datetime(year, month + 1, 1))

    # Query Petty Cash Receipts within the specified year and month
    petty_cash_entries = RMIReceipt.objects.filter(
        received_from='pettycash',
        date__gte=start_date,
        date__lt=end_date
    ).values('petty_cash__payee_name').annotate(
        total_amount=Sum('total_amount')
    )

    for entry in petty_cash_entries:
        row = {
            'from_whom': 'Petty Cash',
            'receipt_no': '-',
            'cash': f"{entry['total_amount']:,}",
            'bank': '-',
        }
        receipts_data.append(row)

    # Query RMI Receipts (non-petty cash) within the specified year and month
    rmi_receipts = RMIReceipt.objects.exclude(
        received_from='pettycash'
    ).filter(
        date__gte=start_date,
        date__lt=end_date
    ).values(
        'received_from', 'cash_bank', 'total_amount'
    )

    for receipt in rmi_receipts:
        row = {
            'from_whom': receipt['received_from'],
            'receipt_no': '-',
            'cash': f"{receipt['total_amount']:,}" if receipt['cash_bank'] == 'cash' else '-',
            'bank': f"{receipt['total_amount']:,}" if receipt['cash_bank'] == 'bank' else '-',
        }
        receipts_data.append(row)

    return {"receipts": receipts_data}

def get_rmi_cashbook(year, month):
    # Initialize a dictionary to store the cashbook data
    cashbook_data = {
        "receipts": [],
        "payments": []
    }

    # Get Receipts (Money In)
    receipts = get_rmi_receipts_money_in(year, month)
    cashbook_data["receipts"].extend(receipts)

    # Get Payments (Money Out)
    payments = get_rmi_payments_money_out(year, month)
    cashbook_data["payments"].extend(payments["payments"])

    return cashbook_data
