from django.urls import path
from .views import CalculateSchoolFundBalancesView, SchoolFundTrialBalanceView

urlpatterns = [
    path('calculate_balances/', CalculateSchoolFundBalancesView.as_view(), name='calculate-school-fund-balances'),
    path('trial-balance/', SchoolFundTrialBalanceView.as_view(), name='school-fund-trial-balance'),
]
