# urls.py
from django.urls import path
from .views import (
    CreatePaymentVoucherView,
    ListPaymentVoucherView,
    PaymentVoucherRetrieveUpdateDestroyView
)

urlpatterns = [
    path('create/', CreatePaymentVoucherView.as_view(), name='create-payment-voucher'),
    path('', ListPaymentVoucherView.as_view(), name='list-payment-vouchers'),
    path('<int:pk>/', PaymentVoucherRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-payment-voucher'),
]
