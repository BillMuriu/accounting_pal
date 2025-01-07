from datetime import datetime
from django.utils import timezone
from django.db.models import Sum
from accounts.school_fund.school_fund_bankcharge.models import SchoolFundBankCharges
from accounts.school_fund.school_fund_paymentvouchers.models import SchoolFundPaymentVoucher
from accounts.school_fund.school_fund_pettycash.models import SchoolFundPettyCash
from accounts.school_fund.school_fund_receipts.models import SchoolFundReceipt
from accounts.school_fund.school_fund_balances.utils import calculate_balance_carried_forward

def get_school_fund_payments_money_out(year, month):
    payments = []
    total_cash_payments = 0
    total_bank_payments = 0
    total_bankcharges = 0

    start_date = timezone.make_aware(datetime(year, month, 1))
    end_date = timezone.make_aware(datetime(year, month + 1, 1)) if month < 12 else timezone.make_aware(datetime(year + 1, 1, 1))

    # Fetch Bank Charges
    bank_charges = SchoolFundBankCharges.objects.filter(charge_date__gte=start_date, charge_date__lt=end_date)
    for charge in bank_charges:
        total_bankcharges += charge.amount
        payments.append({
            "type": "bankcharge",
            "voucher_no": "",
            "cheque_no": "",
            "cash": "",
            "bank": "",
            "bank_charge": charge.amount,
            "date": charge.charge_date
        })

    # Fetch Payment Vouchers
    payment_vouchers = SchoolFundPaymentVoucher.objects.filter(date__gte=start_date, date__lt=end_date)
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
            "date": voucher.date
        })

    # Fetch Petty Cash
    petty_cash_entries = SchoolFundPettyCash.objects.filter(date_issued__gte=start_date, date_issued__lt=end_date)
    for petty_cash in petty_cash_entries:
        total_cash_payments += petty_cash.amount
        payments.append({
            "type": "pettycash",
            "voucher_no": "",
            "cheque_no": petty_cash.cheque_number,
            "cash": petty_cash.amount,
            "bank": "",
            "bank_charge": "",
            "date": petty_cash.date_issued
        })

    total_payments = {
        "total_cash_payments": total_cash_payments,
        "total_bank_payments": total_bank_payments,
        "total_bankcharges": total_bankcharges
    }

    return {"payments": payments, "total_payments": total_payments}


def get_school_fund_receipts_money_in(year, month):
    balance_info = calculate_balance_carried_forward(year, month)

    receipts_data = []
    total_cash_received = 0
    total_bank_received = 0

    balance_forward = {
        'from_whom': 'Balance Carried Forward',
        'receipt_number': '-',
        'cash': f"{balance_info['cashAmount']:,}" if balance_info['cashAmount'] is not None else '-',
        'bank': f"{balance_info['bankAmount']:,}" if balance_info['bankAmount'] is not None else '-',
    }
    receipts_data.append(balance_forward)

    start_date = timezone.make_aware(datetime(year, month, 1))
    end_date = timezone.make_aware(datetime(year, month + 1, 1)) if month < 12 else timezone.make_aware(datetime(year + 1, 1, 1))

    # Fetch Receipts
    school_fund_receipts = SchoolFundReceipt.objects.filter(date__gte=start_date, date__lt=end_date)
    for receipt in school_fund_receipts:
        total_amount = receipt.total_amount or 0
        if receipt.cash_bank == 'cash':
            total_cash_received += total_amount
        elif receipt.cash_bank == 'bank':
            total_bank_received += total_amount

        receipts_data.append({
            'from_whom': receipt.received_from,
            'receipt_number': receipt.receipt_number,
            'cash': f"{total_amount:,}" if receipt.cash_bank == 'cash' else '-',
            'bank': f"{total_amount:,}" if receipt.cash_bank == 'bank' else '-',
            'date': receipt.date
        })

    total_receipts = {
        "total_cash_received": total_cash_received,
        "total_bank_received": total_bank_received
    }

    return {"receipts": receipts_data, "total_receipts": total_receipts}


def get_school_fund_cashbook(year, month):
    cashbook_data = {
        "receipts": [],
        "payments": []
    }

    # Get Receipts (Money In)
    receipts = get_school_fund_receipts_money_in(year, month)
    cashbook_data["receipts"].extend(receipts["receipts"])

    # Get Payments (Money Out)
    payments = get_school_fund_payments_money_out(year, month)
    cashbook_data["payments"].extend(payments["payments"])

    # Add total_receipts and total_payments
    cashbook_data["total_receipts"] = receipts["total_receipts"]
    cashbook_data["total_payments"] = payments["total_payments"]

    return cashbook_data
