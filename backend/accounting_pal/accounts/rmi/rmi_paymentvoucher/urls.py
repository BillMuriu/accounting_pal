from django.urls import path
from .views import ListCreateRMIPaymentVoucherView, RMIPaymentVoucherRetrieveUpdateDestroyView

urlpatterns = [
    path('', ListCreateRMIPaymentVoucherView.as_view(), name='list-create-rmi-payment-voucher'),
    path('<int:pk>/', RMIPaymentVoucherRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-rmi-payment-voucher'),
]
