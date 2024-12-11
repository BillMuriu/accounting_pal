from django.urls import path
from .views import RMIPaymentsMoneyOutView, RMIReceiptsMoneyInView, RMICashbookView

urlpatterns = [
    path('', RMICashbookView.as_view(), name='rmi-cashbook'),
    path('payments/', RMIPaymentsMoneyOutView.as_view(), name='rmi-payments-money-out'),
    path('receipts/', RMIReceiptsMoneyInView.as_view(), name='rmi-receipts-money-in'),
]
