from rest_framework import generics
from .models import OperationReceipt
from .serializers import OperationReceiptSerializer

class CreateOperationReceiptView(generics.CreateAPIView):
    queryset = OperationReceipt.objects.all()
    serializer_class = OperationReceiptSerializer

class ListOperationReceiptView(generics.ListAPIView):
    queryset = OperationReceipt.objects.all()
    serializer_class = OperationReceiptSerializer

class RetrieveOperationReceiptView(generics.RetrieveAPIView):
    queryset = OperationReceipt.objects.all()
    serializer_class = OperationReceiptSerializer

class UpdateOperationReceiptView(generics.UpdateAPIView):
    queryset = OperationReceipt.objects.all()
    serializer_class = OperationReceiptSerializer

class DeleteOperationReceiptView(generics.DestroyAPIView):
    queryset = OperationReceipt.objects.all()
    serializer_class = OperationReceiptSerializer
