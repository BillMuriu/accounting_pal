from django.urls import path
from .views import StudentOpeningBalanceListCreateView, StudentOpeningBalanceRetrieveUpdateDestroyView

urlpatterns = [
    path('', StudentOpeningBalanceListCreateView.as_view(), name='student-opening-balance-list-create'),
    path('<int:id>/', StudentOpeningBalanceRetrieveUpdateDestroyView.as_view(), name='student-opening-balance-detail'),
]
