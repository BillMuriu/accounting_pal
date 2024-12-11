from rest_framework import generics
from .models import SchoolFundReceipt
from .serializers import SchoolFundReceiptSerializer

class SchoolFundReceiptListCreateView(generics.ListCreateAPIView):
    queryset = SchoolFundReceipt.objects.all()
    serializer_class = SchoolFundReceiptSerializer

class SchoolFundReceiptRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolFundReceipt.objects.all()
    serializer_class = SchoolFundReceiptSerializer
    lookup_field = 'id'
