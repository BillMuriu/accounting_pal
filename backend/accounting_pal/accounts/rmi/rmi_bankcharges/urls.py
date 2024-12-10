from django.urls import path
from .views import (
    ListCreateRMIBankChargeView,
    RMIBankChargeRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', ListCreateRMIBankChargeView.as_view(), name='list-create-rmi-bank-charge'),
    path('<int:pk>/', RMIBankChargeRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-rmi-bank-charge'),
]
