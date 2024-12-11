from django.urls import path
from .views import TuitionPaymentsMoneyOutView, TuitionReceiptsMoneyInView, TuitionCashbookView

urlpatterns = [
    path('', TuitionCashbookView.as_view(), name='tuition-cashbook'),
    path('payments/', TuitionPaymentsMoneyOutView.as_view(), name='tuition-payments-money-out'),
    path('receipts/', TuitionReceiptsMoneyInView.as_view(), name='tuition-receipts-money-in'),
]
