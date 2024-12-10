from django.urls import path
from .views import CalculateBalancesView, TrialBalanceView

urlpatterns = [
    path('calculate_balances/', CalculateBalancesView.as_view(), name='calculate-balances'),
    path('trial-balance/', TrialBalanceView.as_view(), name='trial-balance'),
]
