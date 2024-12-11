from datetime import datetime
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal
from accounts.rmi.rmi_bankcharges.models import RMIBankCharge
from accounts.rmi.rmi_paymentvoucher.models import RMIPaymentVoucher  # Adjusted import for RMI
from accounts.rmi.rmi_pettycash.models import RMIPettyCash  # Adjusted import for RMI
from accounts.rmi.rmi_receipts.models import RMIReceipt  # Adjusted import for RMI
from .models import RMIOpeningBalance  # Adjusted for RMI

def calculate_rmi_running_balance(account):
    # Set the current date to now
    current_date = datetime.now().date()

    # Fetch the opening balance directly from the database
    try:
        opening_balance = RMIOpeningBalance.objects.first()
        if opening_balance:
            bank_amount = opening_balance.bank_amount
            cash_amount = opening_balance.cash_amount
        else:
            bank_amount = 0.0
            cash_amount = 0.0
    except RMIOpeningBalance.DoesNotExist:
        bank_amount = 0.0
        cash_amount = 0.0

    # Total bank receipts without year filtering
    total_bank_receipts = RMIReceipt.objects.filter(
        cash_bank='bank'
    ).aggregate(total=Sum('total_amount'))['total'] or 0

    # Total cash receipts without year filtering
    total_cash_receipts = RMIReceipt.objects.filter(
        cash_bank='cash'
    ).aggregate(total=Sum('total_amount'))['total'] or 0

    # Total bank charges without year filtering
    total_bank_charges = RMIBankCharge.objects.aggregate(total=Sum('amount'))['total'] or 0

    # Total petty cash without year filtering
    total_petty_cash = RMIPettyCash.objects.aggregate(total=Sum('amount'))['total'] or 0

    # Total bank payment vouchers without year filtering
    total_bank_payment_vouchers = RMIPaymentVoucher.objects.filter(
        payment_mode='bank'
    ).aggregate(total=Sum('amount_shs'))['total'] or 0

    # Total cash payment vouchers without year filtering
    total_cash_payment_vouchers = RMIPaymentVoucher.objects.filter(
        payment_mode='cash'
    ).aggregate(total=Sum('amount_shs'))['total'] or 0

    # Calculate bank and cash amounts
    bank_amount += total_bank_receipts - (
        total_bank_charges + total_petty_cash + total_bank_payment_vouchers
    )
    cash_amount += total_cash_receipts - total_cash_payment_vouchers

    # Return the running balance dictionary
    return {
        "account": account,
        "date": current_date.isoformat(),
        "bankAmount": bank_amount,
        "cashAmount": cash_amount,
    }


def calculate_rmi_balance_carried_forward(year, month):
    # Define the first day of the specified month and year
    start_date = timezone.make_aware(datetime(year, month, 1))

    # Fetch the opening balance that is applicable before the start date
    opening_balance = (
        RMIOpeningBalance.objects.filter(date__lt=start_date)
        .order_by('-date')
        .first()
    )

    # Initialize bank and cash amounts
    bank_amount = Decimal('0.0')
    cash_amount = Decimal('0.0')

    # Only include the opening balance if it is on or after the start date
    # Include the opening balance if it is on or before the start date
    if opening_balance and opening_balance.date < start_date:
        bank_amount += opening_balance.bank_amount
        cash_amount += opening_balance.cash_amount

    # Total bank receipts up to the day before the specified date
    total_bank_receipts = RMIReceipt.objects.filter(
        date__lt=start_date,
        cash_bank='bank'
    ).aggregate(total=Sum('total_amount'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Total cash receipts up to the day before the specified date
    total_cash_receipts = RMIReceipt.objects.filter(
        date__lt=start_date,
        cash_bank='cash'
    ).aggregate(total=Sum('total_amount'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Total bank charges up to the day before the specified date
    total_bank_charges = RMIBankCharge.objects.filter(
        charge_date__lt=start_date
    ).aggregate(total=Sum('amount'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Total petty cash issued up to the day before the specified date
    total_petty_cash = RMIPettyCash.objects.filter(
        date_issued__lt=start_date
    ).aggregate(total=Sum('amount'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Total bank payment vouchers up to the day before the specified date
    total_bank_payment_vouchers = RMIPaymentVoucher.objects.filter(
        date__lt=start_date,
        payment_mode='bank'
    ).aggregate(total=Sum('amount_shs'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Total cash payment vouchers up to the day before the specified date
    total_cash_payment_vouchers = RMIPaymentVoucher.objects.filter(
        date__lt=start_date,
        payment_mode='cash'
    ).aggregate(total=Sum('amount_shs'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Calculate bank and cash amounts as of the start date (excluding the first day of the month)
    bank_amount += total_bank_receipts - (
        total_bank_charges + total_petty_cash + total_bank_payment_vouchers
    )
    cash_amount += total_cash_receipts - total_cash_payment_vouchers

    # Return the balance carried forward dictionary
    return {
        "account": "rmi",  # Adjusted account name
        "date": start_date.isoformat(),
        "bankAmount": bank_amount,
        "cashAmount": cash_amount,
    }
