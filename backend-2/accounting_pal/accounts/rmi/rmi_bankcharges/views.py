from rest_framework import generics
from .models import RMIBankCharge
from .serializers import RMIBankChargeSerializer

class ListCreateRMIBankChargeView(generics.ListCreateAPIView):
    queryset = RMIBankCharge.objects.all()
    serializer_class = RMIBankChargeSerializer

    def perform_create(self, serializer):
        # Save the RMIBankCharge instance
        rmi_bank_charge = serializer.save()
        print(f"Saved RMI Bank Charge: {rmi_bank_charge}")

class RMIBankChargeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RMIBankCharge.objects.all()
    serializer_class = RMIBankChargeSerializer

    def perform_update(self, serializer):
        rmi_bank_charge = serializer.save()
        print(f'Updated RMI Bank Charge: {rmi_bank_charge}')

    def perform_destroy(self, instance):
        instance.delete()
        print(f'Deleted RMI Bank Charge: {instance}')
