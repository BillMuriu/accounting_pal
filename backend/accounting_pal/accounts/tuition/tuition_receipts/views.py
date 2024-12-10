from rest_framework import generics
from .models import TuitionReceipt  # Import the TuitionReceipt model
from .serializers import TuitionReceiptSerializer  # Import the corresponding serializer

class TuitionReceiptListCreateView(generics.ListCreateAPIView):
    queryset = TuitionReceipt.objects.all()
    serializer_class = TuitionReceiptSerializer

class TuitionReceiptRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TuitionReceipt.objects.all()
    serializer_class = TuitionReceiptSerializer
    lookup_field = 'id'
