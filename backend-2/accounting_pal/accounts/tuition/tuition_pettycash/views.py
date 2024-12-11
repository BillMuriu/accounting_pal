from rest_framework import generics
from rest_framework.response import Response
from .models import TuitionPettyCash
from .serializers import TuitionPettyCashSerializer
from accounts.tuition.tuition_receipts.models import TuitionReceipt

class TuitionPettyCashListCreateView(generics.ListCreateAPIView):
    queryset = TuitionPettyCash.objects.all()
    serializer_class = TuitionPettyCashSerializer

    def perform_create(self, serializer):
        # Save the petty cash instance
        tuition_petty_cash = serializer.save()
        
        # Create a corresponding TuitionReceipt
        receipt = TuitionReceipt.objects.create(
            account=tuition_petty_cash.account,
            received_from='pettycash',
            cash_bank='cash',
            total_amount=tuition_petty_cash.amount,
            date=tuition_petty_cash.date_issued,
            petty_cash=tuition_petty_cash
        )
        
        # Optionally, update the TuitionPettyCash instance with the receipt if needed
        tuition_petty_cash.tuition_receipt = receipt
        tuition_petty_cash.save()

class TuitionPettyCashRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TuitionPettyCash.objects.all()
    serializer_class = TuitionPettyCashSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        tuition_petty_cash = self.get_object()

        # Get the old values before update
        old_amount = tuition_petty_cash.amount
        old_date = tuition_petty_cash.date_issued

        # Update TuitionPettyCash instance
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(tuition_petty_cash, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Update corresponding TuitionReceipt if it exists
        receipt = tuition_petty_cash.tuition_receipt
        if receipt:
            receipt.total_amount = serializer.validated_data.get('amount', old_amount)
            receipt.date = serializer.validated_data.get('date_issued', old_date)
            receipt.save()

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        tuition_petty_cash = self.get_object()

        # Delete the associated TuitionReceipt if it exists
        receipt = tuition_petty_cash.tuition_receipt
        if receipt:
            receipt.delete()

        # Delete the TuitionPettyCash instance
        return super().destroy(request, *args, **kwargs)
