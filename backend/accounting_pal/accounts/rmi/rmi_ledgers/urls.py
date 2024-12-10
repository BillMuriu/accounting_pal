from django.urls import path
from .views import OperationsLedgerView, OtherVoteheadsLedgerView, SchoolFundLedgerView, TuitionLedgerView, BankChargeLedgerView

urlpatterns = [
    path('operations-ledger/', OperationsLedgerView.as_view(), name='operations-ledger'),
    path('other-voteheads-ledger/', OtherVoteheadsLedgerView.as_view(), name='other-voteheads-ledger'),
    path('schoolfund-legder/', SchoolFundLedgerView.as_view(), name='schoolfund-ledger'),
    path('tuition-ledger/', TuitionLedgerView.as_view(), name='tuition-ledger'),
    path('bankcharge-ledger/', BankChargeLedgerView.as_view(), name='bankcharge-ledger'),
]
