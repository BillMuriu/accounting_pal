from django.urls import path
from .views import (
    SchoolFundRMILedgerView,
    SchoolFundBankChargeLedgerView,
    SchoolFundTuitionLedgerView,
    SchoolFundOtherVoteheadsLedgerView,
    SchoolFundCombinedLedgerView,
    SchoolFundOperationsLedgerView,
)

urlpatterns = [
    path('rmi-ledger/', SchoolFundRMILedgerView.as_view(), name='school-fund-rmi-ledger'),
    path('bankcharge-ledger/', SchoolFundBankChargeLedgerView.as_view(), name='school-fund-bankcharge-ledger'),
    path('tuition-ledger/', SchoolFundTuitionLedgerView.as_view(), name='school-fund-tuition-ledger'),
    path('other-voteheads-ledger/', SchoolFundOtherVoteheadsLedgerView.as_view(), name='school-fund-other-voteheads-ledger'),
    path('combined-ledger/', SchoolFundCombinedLedgerView.as_view(), name='school-fund-combined-ledger'),
    path('operations-ledger/', SchoolFundOperationsLedgerView.as_view(), name='school-fund-operations-ledger'),
]
