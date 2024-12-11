from django.urls import path
from .views import ListCreateSchoolFundPaymentVoucherView, SchoolFundPaymentVoucherRetrieveUpdateDestroyView

urlpatterns = [
    path('', ListCreateSchoolFundPaymentVoucherView.as_view(), name='schoolfundpaymentvoucher-list-create'),
    path('<int:pk>/', SchoolFundPaymentVoucherRetrieveUpdateDestroyView.as_view(), name='schoolfundpaymentvoucher-detail'),
]
