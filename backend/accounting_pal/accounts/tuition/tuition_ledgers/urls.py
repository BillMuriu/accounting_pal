from django.urls import path
from .views import OperationsLedgerView, RmiLedgerView, SchoolFundLedgerView, OtherVoteheadsLedgerView, BankChargeLedgerView

urlpatterns = [
    path('operations-ledger/', OperationsLedgerView.as_view(), name='tuition_operations_ledger'),
    path('rmi-ledger/', RmiLedgerView.as_view(), name='rmi-operations-ledger'),
    path('schoolfund-legder/', SchoolFundLedgerView.as_view(), name='schoolfund-ledger'),
    path('other-voteheads-ledger/', OtherVoteheadsLedgerView.as_view(), name='other-voteheads-ledger'),
    path('bankcharge-ledger/', BankChargeLedgerView.as_view(), name='bankcharge-ledger'),
]
