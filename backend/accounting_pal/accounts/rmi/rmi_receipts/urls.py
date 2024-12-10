from django.urls import path
from .views import RMIReceiptListCreateView, RMIReceiptRetrieveUpdateDestroyView

urlpatterns = [
    path('', RMIReceiptListCreateView.as_view(), name='rmi-receipt-list-create'),
    path('<int:id>/', RMIReceiptRetrieveUpdateDestroyView.as_view(), name='rmi-receipt-detail'),
]
