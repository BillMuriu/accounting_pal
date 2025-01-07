from django.urls import path
from .views import (
    SchoolFundOpeningBalanceListCreateView, SchoolFundOpeningBalanceRetrieveUpdateDestroyView, RunningBalanceView, BalanceCarriedForwardView
)

urlpatterns = [
    # School Fund Opening Balance URLs
    path('school-fund-opening-balances/', SchoolFundOpeningBalanceListCreateView.as_view(), name='school-fund-opening-balance-list-create'),
    path('school-fund-opening-balances/<int:pk>/', SchoolFundOpeningBalanceRetrieveUpdateDestroyView.as_view(), name='school-fund-opening-balance-detail'),

    # Running Balance URL (for School Fund)
    path('running-balance/', RunningBalanceView.as_view(), name='running-balance'),

    # Balance Carried Forward URL (for School Fund)
    path('balance-carried-forward/', BalanceCarriedForwardView.as_view(), name='balance-carried-forward'),
]
