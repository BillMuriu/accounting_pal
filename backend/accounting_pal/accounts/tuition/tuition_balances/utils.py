from datetime import datetime
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal
from accounts.tuition.tuition_bankcharges.models import TuitionBankCharge  # Adjusted import for Tuition
from accounts.tuition.tuition_paymentvouchers.models import TuitionPaymentVoucher  # Adjusted import for Tuition
from accounts.tuition.tuition_pettycash.models import TuitionPettyCash  # Adjusted import for Tuition
from accounts.tuition.tuition_receipts.models import TuitionReceipt  # Adjusted import for Tuition
from .models import TuitionOpeningBalance  # Adjusted for Tuition

def calculate_tuition_running_balance(account):
    # Set the current date to now
    current_date = datetime.now().date()

    # Fetch the opening balance directly from the database
    try:
        opening_balance = TuitionOpeningBalance.objects.first()
        if opening_balance:
            bank_amount = Decimal(opening_balance.bank_amount)  # Ensure it's Decimal
            cash_amount = Decimal(opening_balance.cash_amount)  # Ensure it's Decimal
        else:
            bank_amount = Decimal('0.0')
            cash_amount = Decimal('0.0')
    except TuitionOpeningBalance.DoesNotExist:
        bank_amount = Decimal('0.0')
        cash_amount = Decimal('0.0')

    # Total bank receipts without year filtering
    total_bank_receipts = TuitionReceipt.objects.filter(
        cash_bank='bank'
    ).aggregate(total=Sum('total_amount'))['total'] or Decimal('0.0')  # Ensure it's Decimal

    # Total cash receipts without year filtering
    total_cash_receipts = TuitionReceipt.objects.filter(
        cash_bank='cash'
    ).aggregate(total=Sum('total_amount'))['total'] or Decimal('0.0')  # Ensure it's Decimal

    # Total bank charges without year filtering
    total_bank_charges = TuitionBankCharge.objects.aggregate(total=Sum('amount'))['total'] or Decimal('0.0')  # Ensure it's Decimal

    # Total petty cash without year filtering
    total_petty_cash = TuitionPettyCash.objects.aggregate(total=Sum('amount'))['total'] or Decimal('0.0')  # Ensure it's Decimal

    # Total bank payment vouchers without year filtering
    total_bank_payment_vouchers = TuitionPaymentVoucher.objects.filter(
        payment_mode='bank'
    ).aggregate(total=Sum('amount_shs'))['total'] or Decimal('0.0')  # Ensure it's Decimal

    # Total cash payment vouchers without year filtering
    total_cash_payment_vouchers = TuitionPaymentVoucher.objects.filter(
        payment_mode='cash'
    ).aggregate(total=Sum('amount_shs'))['total'] or Decimal('0.0')  # Ensure it's Decimal

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



def calculate_tuition_balance_carried_forward(year, month):
    # Define the first day of the specified month and year
    start_date = timezone.make_aware(datetime(year, month, 1))

    # Fetch the opening balance that is applicable before the start date
    opening_balance = (
        TuitionOpeningBalance.objects.filter(date__lt=start_date)
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
    total_bank_receipts = TuitionReceipt.objects.filter(
        date__lt=start_date,
        cash_bank='bank'
    ).aggregate(total=Sum('total_amount'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Total cash receipts up to the day before the specified date
    total_cash_receipts = TuitionReceipt.objects.filter(
        date__lt=start_date,
        cash_bank='cash'
    ).aggregate(total=Sum('total_amount'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Total bank charges up to the day before the specified date
    total_bank_charges = TuitionBankCharge.objects.filter(
        charge_date__lt=start_date
    ).aggregate(total=Sum('amount'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Total petty cash issued up to the day before the specified date
    total_petty_cash = TuitionPettyCash.objects.filter(
        date_issued__lt=start_date
    ).aggregate(total=Sum('amount'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Total bank payment vouchers up to the day before the specified date
    total_bank_payment_vouchers = TuitionPaymentVoucher.objects.filter(
        date__lt=start_date,
        payment_mode='bank'
    ).aggregate(total=Sum('amount_shs'))['total'] or Decimal('0')  # Ensure it’s Decimal

    # Total cash payment vouchers up to the day before the specified date
    total_cash_payment_vouchers = TuitionPaymentVoucher.objects.filter(
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
        "account": "tuition",  # Adjusted account name
        "date": start_date.isoformat(),
        "bankAmount": bank_amount,
        "cashAmount": cash_amount,
    }
