from django.urls import path
from .views import SchoolFundBankChargesListCreateView, SchoolFundBankChargesRetrieveUpdateDestroyView

urlpatterns = [
    path('', SchoolFundBankChargesListCreateView.as_view(), name='schoolfundbankcharges-list-create'),
    path('<int:pk>/', SchoolFundBankChargesRetrieveUpdateDestroyView.as_view(), name='schoolfundbankcharges-detail'),
]
