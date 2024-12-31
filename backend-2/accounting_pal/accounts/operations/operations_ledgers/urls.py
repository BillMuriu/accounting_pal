from django.urls import path
from .views import RMILedgerView, BankChargeLedgerView, SchoolFundLedgerView, TuitionLedgerView, OtherVoteheadsLedgerView, CombinedLedgerView

urlpatterns = [
    path('rmi-ledger/', RMILedgerView.as_view(), name='rmi-ledger'),
    path('bankcharge-ledger/', BankChargeLedgerView.as_view(), name='bankcharge-ledger'),
    path('school-fund-ledger/', SchoolFundLedgerView.as_view(), name='school-fund-ledger'),
    path('tuition-ledger/', TuitionLedgerView.as_view(), name='tuition-ledger'),
    path('other-voteheads-ledger/', OtherVoteheadsLedgerView.as_view(), name='other-voteheads-ledger'),
    path('combined-ledger/', CombinedLedgerView.as_view(), name='combined-ledger'),
]
