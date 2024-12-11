from django.urls import path
from .views import SchoolFundReceiptListCreateView, SchoolFundReceiptRetrieveUpdateDestroyView

urlpatterns = [
    path('', SchoolFundReceiptListCreateView.as_view(), name='school-fund-receipt-list-create'),
    path('<int:id>/', SchoolFundReceiptRetrieveUpdateDestroyView.as_view(), name='school-fund-receipt-detail'),
]
