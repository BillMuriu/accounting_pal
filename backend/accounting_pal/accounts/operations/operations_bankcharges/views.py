from rest_framework import generics
from .models import BankCharges
from .serializers import BankChargesSerializer

class BankChargesListCreateView(generics.ListCreateAPIView):
    queryset = BankCharges.objects.all()
    serializer_class = BankChargesSerializer

class BankChargesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankCharges.objects.all()
    serializer_class = BankChargesSerializer
