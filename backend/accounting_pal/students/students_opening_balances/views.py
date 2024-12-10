# finances/views.py
from rest_framework import generics
from .models import StudentOpeningBalance
from .serializers import StudentOpeningBalanceSerializer

class StudentOpeningBalanceListCreateView(generics.ListCreateAPIView):
    queryset = StudentOpeningBalance.objects.all()
    serializer_class = StudentOpeningBalanceSerializer

class StudentOpeningBalanceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentOpeningBalance.objects.all()
    serializer_class = StudentOpeningBalanceSerializer
    lookup_field = 'id'
