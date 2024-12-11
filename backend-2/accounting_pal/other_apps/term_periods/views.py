from rest_framework import generics
from .models import TermPeriod
from .serializers import TermPeriodSerializer

class TermPeriodListCreateView(generics.ListCreateAPIView):
    queryset = TermPeriod.objects.all()
    serializer_class = TermPeriodSerializer

class TermPeriodRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TermPeriod.objects.all()
    serializer_class = TermPeriodSerializer
    lookup_field = 'id'
