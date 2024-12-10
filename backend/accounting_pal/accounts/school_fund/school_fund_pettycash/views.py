# views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import SchoolFundPettyCash
from .serializers import SchoolFundPettyCashSerializer
from accounts.school_fund.school_fund_receipts.models import SchoolFundReceipt

class SchoolFundPettyCashListCreateView(generics.ListCreateAPIView):
    queryset = SchoolFundPettyCash.objects.all()
    serializer_class = SchoolFundPettyCashSerializer

    def perform_create(self, serializer):
        school_fund_petty_cash = serializer.save()
        
        # Create a corresponding SchoolFundReceipt
        receipt = SchoolFundReceipt.objects.create(
            account=school_fund_petty_cash.account,
            received_from='pettycash',
            cash_bank='cash',
            total_amount=school_fund_petty_cash.amount,
            date=school_fund_petty_cash.date_issued,
            petty_cash=school_fund_petty_cash
        )
        
        # Optionally, update the SchoolFundPettyCash instance with the receipt id if needed
        school_fund_petty_cash.school_fund_receipt = receipt
        school_fund_petty_cash.save()

class SchoolFundPettyCashRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolFundPettyCash.objects.all()
    serializer_class = SchoolFundPettyCashSerializer

    def update(self, request, *args, **kwargs):
        school_fund_petty_cash = self.get_object()

        # Get the old values before update
        old_amount = school_fund_petty_cash.amount
        old_date = school_fund_petty_cash.date_issued
        
        # Update SchoolFundPettyCash instance
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(school_fund_petty_cash, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Update corresponding SchoolFundReceipt
        receipt = school_fund_petty_cash.school_fund_receipt
        if receipt:
            receipt.total_amount = serializer.validated_data.get('amount', old_amount)
            receipt.date = serializer.validated_data.get('date_issued', old_date)
            receipt.save()

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        school_fund_petty_cash = self.get_object()

        # Delete the associated SchoolFundReceipt if it exists
        receipt = school_fund_petty_cash.school_fund_receipt
        if receipt:
            receipt.delete()

        # Delete the SchoolFundPettyCash instance
        return super().destroy(request, *args, **kwargs)
