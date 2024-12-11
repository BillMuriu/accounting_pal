from django.urls import path
from .views import TuitionReceiptListCreateView, TuitionReceiptRetrieveUpdateDestroyView

urlpatterns = [
    path('', TuitionReceiptListCreateView.as_view(), name='tuition-receipt-list-create'),
    path('<int:id>/', TuitionReceiptRetrieveUpdateDestroyView.as_view(), name='tuition-receipt-detail'),
]
