from decimal import Decimal
from django.utils import timezone
from django.db.models import Sum
from accounts.operations.operations_bankcharges.models import BankCharges
from accounts.operations.operations_paymentvouchers.models import PaymentVoucher
from accounts.operations.operations_pettycash.models import PettyCash
from accounts.operations.operations_receipts.models import OperationReceipt
from accounts.operations.operations_balances.models import OpeningBalance


def calculate_balances(start_date, end_date):
    # Ensure both dates are timezone-aware
    if timezone.is_naive(start_date):
        start_date = timezone.make_aware(start_date)
    if timezone.is_naive(end_date):
        end_date = timezone.make_aware(end_date)

    # Calculate Opening Balance
    opening_balance_record = OpeningBalance.objects.filter(date__lt=start_date).order_by('-date').first()
    
    if opening_balance_record:
        opening_bank_amount = Decimal(opening_balance_record.bank_amount)
        opening_cash_amount = Decimal(opening_balance_record.cash_amount)
    else:
        opening_bank_amount = Decimal(0.0)
        opening_cash_amount = Decimal(0.0)

    # Total bank receipts up to the start date
    total_bank_receipts_start = Decimal(OperationReceipt.objects.filter(
        cash_bank='bank',
        date__lt=start_date
    ).aggregate(total=Sum('total_amount'))['total'] or 0)

    # Total cash receipts up to the start date
    total_cash_receipts_start = Decimal(OperationReceipt.objects.filter(
        cash_bank='cash',
        date__lt=start_date
    ).aggregate(total=Sum('total_amount'))['total'] or 0)

    # Total bank charges up to the start date
    total_bank_charges_start = Decimal(BankCharges.objects.filter(
        charge_date__lt=start_date
    ).aggregate(total=Sum('amount'))['total'] or 0)

    # Total petty cash up to the start date
    total_petty_cash_start = Decimal(PettyCash.objects.filter(
        date_issued__lt=start_date
    ).aggregate(total=Sum('amount'))['total'] or 0)

    # Total bank payment vouchers up to the start date
    total_bank_payment_vouchers_start = Decimal(PaymentVoucher.objects.filter(
        payment_mode='bank',
        date__lt=start_date
    ).aggregate(total=Sum('amount_shs'))['total'] or 0)

    # Total cash payment vouchers up to the start date
    total_cash_payment_vouchers_start = Decimal(PaymentVoucher.objects.filter(
        payment_mode='cash',
        date__lt=start_date
    ).aggregate(total=Sum('amount_shs'))['total'] or 0)

    # Calculate opening balances
    opening_bank_amount += total_bank_receipts_start - (
        total_bank_charges_start + total_petty_cash_start + total_bank_payment_vouchers_start
    )
    opening_cash_amount += total_cash_receipts_start - total_cash_payment_vouchers_start

    # Create opening balance result
    opening_balance_result = {
        "date": start_date.isoformat(),
        "bankAmount": opening_bank_amount,
        "cashAmount": opening_cash_amount,
    }

    # Calculate Closing Balance
    closing_balance_record = OpeningBalance.objects.filter(date__lte=end_date).order_by('-date').first()
    
    if closing_balance_record:
        closing_bank_amount = Decimal(closing_balance_record.bank_amount)
        closing_cash_amount = Decimal(closing_balance_record.cash_amount)
    else:
        closing_bank_amount = Decimal(0.0)
        closing_cash_amount = Decimal(0.0)

    # Total bank receipts up to the end date
    total_bank_receipts_end = Decimal(OperationReceipt.objects.filter(
        cash_bank='bank',
        date__lte=end_date
    ).aggregate(total=Sum('total_amount'))['total'] or 0)

    # Total cash receipts up to the end date
    total_cash_receipts_end = Decimal(OperationReceipt.objects.filter(
        cash_bank='cash',
        date__lte=end_date
    ).aggregate(total=Sum('total_amount'))['total'] or 0)

    # Total bank charges up to the end date
    total_bank_charges_end = Decimal(BankCharges.objects.filter(
        charge_date__lte=end_date
    ).aggregate(total=Sum('amount'))['total'] or 0)

    # Total petty cash up to the end date
    total_petty_cash_end = Decimal(PettyCash.objects.filter(
        date_issued__lte=end_date
    ).aggregate(total=Sum('amount'))['total'] or 0)

    # Total bank payment vouchers up to the end date
    total_bank_payment_vouchers_end = Decimal(PaymentVoucher.objects.filter(
        payment_mode='bank',
        date__lte=end_date
    ).aggregate(total=Sum('amount_shs'))['total'] or 0)

    # Total cash payment vouchers up to the end date
    total_cash_payment_vouchers_end = Decimal(PaymentVoucher.objects.filter(
        payment_mode='cash',
        date__lte=end_date
    ).aggregate(total=Sum('amount_shs'))['total'] or 0)

    # Calculate closing balances
    closing_bank_amount += total_bank_receipts_end - (
        total_bank_charges_end + total_petty_cash_end + total_bank_payment_vouchers_end
    )
    closing_cash_amount += total_cash_receipts_end - total_cash_payment_vouchers_end

    # Create closing balance result
    closing_balance_result = {
        "date": end_date.isoformat(),
        "bankAmount": closing_bank_amount,
        "cashAmount": closing_cash_amount,
    }

    # Return the balances in the desired nested list format
    return [
        {
            "openingBalance": opening_balance_result
        },
        {
            "closingBalance": closing_balance_result
        }
    ]