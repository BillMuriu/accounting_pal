from django.utils import timezone
from accounts.school_fund.school_fund_receipts.models import SchoolFundReceipt
from accounts.school_fund.school_fund_paymentvouchers.models import SchoolFundPaymentVoucher


# Function to get school fund rmi debits
def get_school_fund_rmi_debits(start_date, end_date):
    debits = []

    # Ensure the dates are timezone-aware only if they're naive
    if timezone.is_naive(start_date):
        start_date = timezone.make_aware(start_date)
    if timezone.is_naive(end_date):
        end_date = timezone.make_aware(end_date)

    # Fetch Payment Vouchers within the specified period where vote_head is 'rmi'
    payment_vouchers = SchoolFundPaymentVoucher.objects.filter(
        date__gte=start_date, date__lt=end_date, vote_head='rmi'
    )

    # Loop through the filtered vouchers and create debit entries (date, amount, and cashbook)
    for voucher in payment_vouchers:
        debits.append({
            "date": voucher.date,
            "amount": voucher.amount_shs,
            "cashbook": get_cashbook(voucher.date)  # Generate cashbook based on the date
        })

    return debits


# Function to get school fund rmi credits
def get_school_fund_rmi_credits(start_date, end_date):
    credits = []

    # Ensure the dates are timezone-aware only if they're naive
    if timezone.is_naive(start_date):
        start_date = timezone.make_aware(start_date)
    if timezone.is_naive(end_date):
        end_date = timezone.make_aware(end_date)

    # Fetch School Fund Receipts within the specified period where received_from is 'rmi'
    school_fund_receipts = SchoolFundReceipt.objects.filter(
        date__gte=start_date, date__lt=end_date, received_from='rmi'
    )

    # Loop through the filtered receipts and create credit entries (date, amount, and cashbook)
    for receipt in school_fund_receipts:
        credits.append({
            "date": receipt.date,
            "amount": receipt.rmi_fund,
            "cashbook": get_cashbook(receipt.date)  # Generate cashbook based on the date
        })

    return credits


# Function to get school fund rmi ledger with debits and credits
def get_school_fund_rmi_ledger(start_date, end_date):
    # Get debits and credits
    debits = get_school_fund_rmi_debits(start_date, end_date)
    credits = get_school_fund_rmi_credits(start_date, end_date)

    # Calculate total debits and credits
    total_debits = sum(debit['amount'] for debit in debits)
    total_credits = sum(credit['amount'] for credit in credits)

    # Create a combined ledger with separate lists for credits and debits and their totals
    ledger = {
        "credits": [{"date": credit["date"], "amount": credit["amount"], "type": "credit", "cashbook": credit["cashbook"]} for credit in credits],
        "debits": [{"date": debit["date"], "amount": debit["amount"], "type": "debit", "cashbook": debit["cashbook"]} for debit in debits],
        "total_credits": total_credits,
        "total_debits": total_debits
    }

    return ledger


# Function to generate cashbook based on the date
def get_cashbook(date):
    # Financial year starts on July 1st
    year = date.year
    if date.month >= 7:
        # From July to December, we are in the current financial year
        financial_year = f"{year}-{year + 1}"
        cashbook_no = date.month - 6  # July (7) becomes 1, August (8) becomes 2, etc.
    else:
        # From January to June, we are in the previous financial year
        financial_year = f"{year - 1}-{year}"
        cashbook_no = date.month + 6  # January (1) becomes 7, February (2) becomes 8, etc.

    return f"CashBook-{cashbook_no}-{financial_year}"
