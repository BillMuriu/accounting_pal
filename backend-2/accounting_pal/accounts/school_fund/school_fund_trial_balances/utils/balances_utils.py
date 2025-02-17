from decimal import Decimal
from django.utils import timezone
from django.db.models import Sum
from accounts.school_fund.school_fund_bankcharge.models import SchoolFundBankCharges
from accounts.school_fund.school_fund_paymentvouchers.models import SchoolFundPaymentVoucher
from accounts.school_fund.school_fund_pettycash.models import SchoolFundPettyCash
from accounts.school_fund.school_fund_receipts.models import SchoolFundReceipt
from accounts.school_fund.school_fund_balances.models import SchoolFundOpeningBalance


from decimal import Decimal
from django.utils import timezone
from django.db.models import Sum
from accounts.school_fund.school_fund_bankcharge.models import SchoolFundBankCharges
from accounts.school_fund.school_fund_paymentvouchers.models import SchoolFundPaymentVoucher
from accounts.school_fund.school_fund_pettycash.models import SchoolFundPettyCash
from accounts.school_fund.school_fund_receipts.models import SchoolFundReceipt
from accounts.school_fund.school_fund_balances.models import SchoolFundOpeningBalance


def calculate_school_fund_balances(start_date, end_date):
    # Ensure both dates are timezone-aware
    if timezone.is_naive(start_date):
        start_date = timezone.make_aware(start_date)
    if timezone.is_naive(end_date):
        end_date = timezone.make_aware(end_date)

    # Calculate Opening Balance
    opening_balance_record = SchoolFundOpeningBalance.objects.filter(date__lt=start_date).order_by('-date').first()
    
    if opening_balance_record:
        opening_bank_amount = Decimal(opening_balance_record.bank_amount)
        opening_cash_amount = Decimal(opening_balance_record.cash_amount)
    else:
        opening_bank_amount = Decimal(0.0)
        opening_cash_amount = Decimal(0.0)

    # Total bank receipts up to the start date
    total_bank_receipts_start = Decimal(SchoolFundReceipt.objects.filter(
        cash_bank='bank',
        date__lt=start_date
    ).aggregate(total=Sum('total_amount'))['total'] or 0)

    # Total cash receipts up to the start date
    total_cash_receipts_start = Decimal(SchoolFundReceipt.objects.filter(
        cash_bank='cash',
        date__lt=start_date
    ).aggregate(total=Sum('total_amount'))['total'] or 0)

    # Total bank charges up to the start date
    total_bank_charges_start = Decimal(SchoolFundBankCharges.objects.filter(
        charge_date__lt=start_date
    ).aggregate(total=Sum('amount'))['total'] or 0)

    # Total petty cash up to the start date
    total_petty_cash_start = Decimal(SchoolFundPettyCash.objects.filter(
        date_issued__lt=start_date
    ).aggregate(total=Sum('amount'))['total'] or 0)

    # Total bank payment vouchers up to the start date
    total_bank_payment_vouchers_start = Decimal(SchoolFundPaymentVoucher.objects.filter(
        payment_mode='bank',
        date__lt=start_date
    ).aggregate(total=Sum('amount_shs'))['total'] or 0)

    # Total cash payment vouchers up to the start date
    total_cash_payment_vouchers_start = Decimal(SchoolFundPaymentVoucher.objects.filter(
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
    closing_balance_record = SchoolFundOpeningBalance.objects.filter(date__lte=end_date).order_by('-date').first()
    
    if closing_balance_record:
        closing_bank_amount = Decimal(closing_balance_record.bank_amount)
        closing_cash_amount = Decimal(closing_balance_record.cash_amount)
    else:
        closing_bank_amount = Decimal(0.0)
        closing_cash_amount = Decimal(0.0)

    # Total bank receipts up to the end date
    total_bank_receipts_end = Decimal(SchoolFundReceipt.objects.filter(
        cash_bank='bank',
        date__lte=end_date
    ).aggregate(total=Sum('total_amount'))['total'] or 0)

    # Total cash receipts up to the end date
    total_cash_receipts_end = Decimal(SchoolFundReceipt.objects.filter(
        cash_bank='cash',
        date__lte=end_date
    ).aggregate(total=Sum('total_amount'))['total'] or 0)

    # Total bank charges up to the end date
    total_bank_charges_end = Decimal(SchoolFundBankCharges.objects.filter(
        charge_date__lte=end_date
    ).aggregate(total=Sum('amount'))['total'] or 0)

    # Total petty cash up to the end date
    total_petty_cash_end = Decimal(SchoolFundPettyCash.objects.filter(
        date_issued__lte=end_date
    ).aggregate(total=Sum('amount'))['total'] or 0)

    # Total bank payment vouchers up to the end date
    total_bank_payment_vouchers_end = Decimal(SchoolFundPaymentVoucher.objects.filter(
        payment_mode='bank',
        date__lte=end_date
    ).aggregate(total=Sum('amount_shs'))['total'] or 0)

    # Total cash payment vouchers up to the end date
    total_cash_payment_vouchers_end = Decimal(SchoolFundPaymentVoucher.objects.filter(
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
