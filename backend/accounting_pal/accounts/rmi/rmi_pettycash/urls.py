from django.urls import path
from .views import RMIPettyCashListCreateView, RMIPettyCashRetrieveUpdateDestroyView

urlpatterns = [
    path('', RMIPettyCashListCreateView.as_view(), name='rmi-petty-cash-list-create'),
    path('<int:id>/', RMIPettyCashRetrieveUpdateDestroyView.as_view(), name='rmi-petty-cash-detail'),
]
