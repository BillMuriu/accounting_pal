from django.urls import path
from .views import BankChargesListCreateView, BankChargesRetrieveUpdateDestroyView

urlpatterns = [
    path('', BankChargesListCreateView.as_view(), name='bank-charges-list-create'),
    path('<int:pk>/', BankChargesRetrieveUpdateDestroyView.as_view(), name='bank-charges-detail'),
]
