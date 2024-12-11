# urls.py
from django.urls import path
from .views import CalculateRmiBalancesView, RmiTrialBalanceView

urlpatterns = [
    path('calculate_balances/', CalculateRmiBalancesView.as_view(), name='calculate-rmi-balances'),
    path('trial-balance/', RmiTrialBalanceView.as_view(), name='rmi-trial-balance'),
]
