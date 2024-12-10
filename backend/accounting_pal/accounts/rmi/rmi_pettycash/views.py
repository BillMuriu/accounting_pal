from rest_framework import generics
from rest_framework.response import Response
from .models import RMIPettyCash
from .serializers import RMIPettyCashSerializer
from accounts.rmi.rmi_receipts.models import RMIReceipt


class RMIPettyCashListCreateView(generics.ListCreateAPIView):
    queryset = RMIPettyCash.objects.all()
    serializer_class = RMIPettyCashSerializer

    def perform_create(self, serializer):
        # Save the petty cash instance
        rmi_petty_cash = serializer.save()
        
        # Create a corresponding RMIReceipt
        receipt = RMIReceipt.objects.create(
            account=rmi_petty_cash.account,
            received_from='pettycash',
            cash_bank='cash',
            total_amount=rmi_petty_cash.amount,
            date=rmi_petty_cash.date_issued,
            petty_cash=rmi_petty_cash
        )
        
        # Optionally, update the RMIPettyCash instance with the receipt if needed
        rmi_petty_cash.rmi_receipt = receipt
        rmi_petty_cash.save()

class RMIPettyCashRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RMIPettyCash.objects.all()
    serializer_class = RMIPettyCashSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        rmi_petty_cash = self.get_object()

        # Get the old values before update
        old_amount = rmi_petty_cash.amount
        old_date = rmi_petty_cash.date_issued

        # Update RMIPettyCash instance
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(rmi_petty_cash, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Only update corresponding RMIReceipt if it exists
        if hasattr(rmi_petty_cash, 'rmi_receipt') and rmi_petty_cash.rmi_receipt:
            receipt = rmi_petty_cash.rmi_receipt
            receipt.total_amount = serializer.validated_data.get('amount', old_amount)
            receipt.date = serializer.validated_data.get('date_issued', old_date)
            receipt.save()

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        rmi_petty_cash = self.get_object()

        # Only delete the associated RMIReceipt if it exists
        if hasattr(rmi_petty_cash, 'rmi_receipt') and rmi_petty_cash.rmi_receipt:
            receipt = rmi_petty_cash.rmi_receipt
            receipt.delete()

        # Delete the RMIPettyCash instance
        return super().destroy(request, *args, **kwargs)
