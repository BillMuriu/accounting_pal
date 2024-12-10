from django.urls import path
from .views import (
    TuitionRunningBalanceView,
    TuitionBalanceCarriedForwardView,
    TuitionOpeningBalanceListCreateView,
    TuitionOpeningBalanceRetrieveUpdateDestroyView
)

urlpatterns = [
    path('running-balance/', TuitionRunningBalanceView.as_view(), name='tuition-running-balance'),
    path('balance-carried-forward/', TuitionBalanceCarriedForwardView.as_view(), name='tuition-balance-carried-forward'),
    path('opening-balances/', TuitionOpeningBalanceListCreateView.as_view(), name='tuition-opening-balance-list-create'),
    path('opening-balances/<int:pk>/', TuitionOpeningBalanceRetrieveUpdateDestroyView.as_view(), name='tuition-opening-balance-detail'),
]
