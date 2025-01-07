# urls.py
from django.urls import path
from .views import SchoolFundPaymentsMoneyOutView, SchoolFundReceiptsMoneyInView, SchoolFundCashbookView

urlpatterns = [
    path('payments-money-out/', SchoolFundPaymentsMoneyOutView.as_view(), name='school-fund-payments-money-out'),
    path('receipts-money-in/', SchoolFundReceiptsMoneyInView.as_view(), name='school-fund-receipts-money-in'),
    path('cashbook/', SchoolFundCashbookView.as_view(), name='school-fund-cashbook'),
]
