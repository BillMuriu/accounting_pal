from rest_framework import generics
from .models import TuitionBankCharge
from .serializers import TuitionBankChargeSerializer

class ListCreateTuitionBankChargeView(generics.ListCreateAPIView):
    queryset = TuitionBankCharge.objects.all()
    serializer_class = TuitionBankChargeSerializer

    def perform_create(self, serializer):
        # Save the TuitionBankCharge instance
        tuition_bank_charge = serializer.save()
        print(f"Saved Tuition Bank Charge: {tuition_bank_charge}")

class TuitionBankChargeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TuitionBankCharge.objects.all()
    serializer_class = TuitionBankChargeSerializer

    def perform_update(self, serializer):
        tuition_bank_charge = serializer.save()
        print(f'Updated Tuition Bank Charge: {tuition_bank_charge}')

    def perform_destroy(self, instance):
        instance.delete()
        print(f'Deleted Tuition Bank Charge: {instance}')
