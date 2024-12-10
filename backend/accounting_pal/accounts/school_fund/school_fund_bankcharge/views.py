from rest_framework import generics
from .models import SchoolFundBankCharges
from .serializers import SchoolFundBankChargesSerializer

class SchoolFundBankChargesListCreateView(generics.ListCreateAPIView):
    queryset = SchoolFundBankCharges.objects.all()
    serializer_class = SchoolFundBankChargesSerializer

class SchoolFundBankChargesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolFundBankCharges.objects.all()
    serializer_class = SchoolFundBankChargesSerializer
