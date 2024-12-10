from accounts.operations.operations_ledgers.utils.rmi_ledger_utils import get_rmi_ledger
from accounts.operations.operations_ledgers.utils.other_voteheads_ledger_utils import get_other_voteheads_ledger
from accounts.operations.operations_ledgers.utils.schoolfund_ledger_utils import get_school_fund_ledger
from accounts.operations.operations_ledgers.utils.tuition_ledger_utils import get_tuition_ledger
from accounts.operations.operations_ledgers.utils.bank_charge_ledger_utils import get_bankcharge_ledger
from .balances_utils import calculate_balances

def create_trial_balance(start_date, end_date):
    # Get the total debits and credits for each account, defaulting to 0 if they don't exist
    rmi_ledger = get_rmi_ledger(start_date, end_date)
    other_voteheads_ledger = get_other_voteheads_ledger(start_date, end_date)
    school_fund_ledger = get_school_fund_ledger(start_date, end_date)
    tuition_ledger = get_tuition_ledger(start_date, end_date)
    bankcharge_ledger = get_bankcharge_ledger(start_date, end_date)

    # Get the opening and closing balances for bank and cash
    balances = calculate_balances(start_date, end_date)

    # Ensure opening and closing balances exist
    if len(balances) < 2 or 'closingBalance' not in balances[1] or 'openingBalance' not in balances[0]:
        raise KeyError("Missing key in response: 'openingBalance' or 'closingBalance'")

    # Extract balances
    opening_bank_balance = balances[0]['openingBalance']['bankAmount']
    opening_cash_balance = balances[0]['openingBalance']['cashAmount']
    closing_bank_balance = balances[1]['closingBalance']['bankAmount']
    closing_cash_balance = balances[1]['closingBalance']['cashAmount']

    # Safely get total debits and credits, using 0 if the key is missing
    def safe_get_ledger_total(ledger, key):
        return ledger.get(key, 0)

    # Calculate the total debits
    total_debits = (
        safe_get_ledger_total(rmi_ledger, 'total_debits') +
        safe_get_ledger_total(other_voteheads_ledger, 'total_debits') +
        safe_get_ledger_total(school_fund_ledger, 'total_debits') +
        safe_get_ledger_total(tuition_ledger, 'total_debits') +
        safe_get_ledger_total(bankcharge_ledger, 'total_debits') +
        closing_bank_balance +
        closing_cash_balance
    )

    # Calculate the total credits
    total_credits = (
        safe_get_ledger_total(rmi_ledger, 'total_credits') +
        safe_get_ledger_total(other_voteheads_ledger, 'total_credits') +
        safe_get_ledger_total(school_fund_ledger, 'total_credits') +
        safe_get_ledger_total(tuition_ledger, 'total_credits') +
        safe_get_ledger_total(bankcharge_ledger, 'total_credits') +
        opening_bank_balance +
        opening_cash_balance
    )

    # Create the trial balance structure
    trial_balance = {
        "debits": {
            "RMI": safe_get_ledger_total(rmi_ledger, 'total_debits'),
            "Other Voteheads": safe_get_ledger_total(other_voteheads_ledger, 'total_debits'),
            "School Fund": safe_get_ledger_total(school_fund_ledger, 'total_debits'),
            "Tuition": safe_get_ledger_total(tuition_ledger, 'total_debits'),
            "Bank Charges": safe_get_ledger_total(bankcharge_ledger, 'total_debits'),
            "Closing Bank Balance": {
                "amount": closing_bank_balance,
                "cashbook": "bank"
            },
            "Closing Cash Balance": {
                "amount": closing_cash_balance,
                "cashbook": "cash"
            },
        },
        "credits": {
            "RMI": safe_get_ledger_total(rmi_ledger, 'total_credits'),
            "Other Voteheads": safe_get_ledger_total(other_voteheads_ledger, 'total_credits'),
            "School Fund": safe_get_ledger_total(school_fund_ledger, 'total_credits'),
            "Tuition": safe_get_ledger_total(tuition_ledger, 'total_credits'),
            "Bank Charges": safe_get_ledger_total(bankcharge_ledger, 'total_credits'),
            "Opening Bank Balance": {
                "amount": opening_bank_balance,
                "cashbook": "bank"
            },
            "Opening Cash Balance": {
                "amount": opening_cash_balance,
                "cashbook": "cash"
            },
        },
        "total_debits": total_debits,
        "total_credits": total_credits
    }

    return trial_balance

