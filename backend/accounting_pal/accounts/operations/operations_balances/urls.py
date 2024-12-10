from django.urls import path
from .views import (
    OpeningBalanceListCreateView, OpeningBalanceRetrieveUpdateDestroyView, RunningBalanceView, BalanceCarriedForwardView   
)

urlpatterns = [
    # Opening Balance URLs
    path('opening-balances/', OpeningBalanceListCreateView.as_view(), name='opening-balance-list-create'),
    path('opening-balances/<int:pk>/', OpeningBalanceRetrieveUpdateDestroyView.as_view(), name='opening-balance-detail'),


    path('running-balance/', RunningBalanceView.as_view(), name='running-balance'),
    path('balance-carried-forward/', BalanceCarriedForwardView.as_view(), name='balance-carried-forward'),
]
