from django.urls import path
from .views import ListCreateTuitionBankChargeView, TuitionBankChargeRetrieveUpdateDestroyView

urlpatterns = [
    path('', ListCreateTuitionBankChargeView.as_view(), name='list-create-tuition-bank-charge'),
    path('<int:pk>/', TuitionBankChargeRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-tuition-bank-charge'),
]
