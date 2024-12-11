# urls.py
from django.urls import path
from .views import OperationsPaymentsMoneyOutView, ReceiptsMoneyInView, CashbookView

urlpatterns = [
    path('payments-money-out/', OperationsPaymentsMoneyOutView.as_view(), name='payments-money-out'),
    path('receipts-money-in/', ReceiptsMoneyInView.as_view(), name='receipts-money-in'),
     path('cashbook/', CashbookView.as_view(), name='cashbook'),
]
