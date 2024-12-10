from django.urls import path
from .views import (
    CreateOperationReceiptView,
    ListOperationReceiptView,
    RetrieveOperationReceiptView,
    UpdateOperationReceiptView,
    DeleteOperationReceiptView
)

urlpatterns = [
    path('create/', CreateOperationReceiptView.as_view(), name='create-operation-receipt'),
    path('', ListOperationReceiptView.as_view(), name='list-operation-receipts'),
    path('<int:pk>/', RetrieveOperationReceiptView.as_view(), name='retrieve-operation-receipt'),
    path('<int:pk>/update/', UpdateOperationReceiptView.as_view(), name='update-operation-receipt'),
    path('<int:pk>/delete/', DeleteOperationReceiptView.as_view(), name='delete-operation-receipt'),
]
