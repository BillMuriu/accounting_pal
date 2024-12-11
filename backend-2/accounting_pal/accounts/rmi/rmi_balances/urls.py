from django.urls import path
from .views import (
    RmiRunningBalanceView,
    RmiBalanceCarriedForwardView,
    RmiOpeningBalanceListCreateView,
    RmiOpeningBalanceRetrieveUpdateDestroyView
)

urlpatterns = [
    path('running-balance/', RmiRunningBalanceView.as_view(), name='rmi-running-balance'),
    path('balance-carried-forward/', RmiBalanceCarriedForwardView.as_view(), name='rmi-balance-carried-forward'),
    path('opening-balances/', RmiOpeningBalanceListCreateView.as_view(), name='rmi-opening-balance-list-create'),
    path('opening-balances/<int:pk>/', RmiOpeningBalanceRetrieveUpdateDestroyView.as_view(), name='rmi-opening-balance-detail'),
]
