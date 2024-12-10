from django.urls import path
from .views import (
    ListCreateTuitionPaymentVoucherView,
    TuitionPaymentVoucherRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', ListCreateTuitionPaymentVoucherView.as_view(), name='list-create-tuition-payment-vouchers'),
    path('<int:pk>/', TuitionPaymentVoucherRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-tuition-payment-voucher'),
]
