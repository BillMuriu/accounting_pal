from rest_framework import generics
from .models import RMIReceipt
from .serializers import RMIReceiptSerializer

class RMIReceiptListCreateView(generics.ListCreateAPIView):
    queryset = RMIReceipt.objects.all()
    serializer_class = RMIReceiptSerializer

class RMIReceiptRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RMIReceipt.objects.all()
    serializer_class = RMIReceiptSerializer
    lookup_field = 'id'
