from rest_framework import serializers
from .models import SchoolFundPettyCash
from accounts.school_fund.school_fund_receipts.models import SchoolFundReceipt

class SchoolFundReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolFundReceipt
        fields = ['id', 'account', 'received_from', 'cash_bank', 'total_amount', 'date']

class SchoolFundPettyCashSerializer(serializers.ModelSerializer):
    school_fund_receipt = SchoolFundReceiptSerializer(read_only=True)  # Include nested serializer

    class Meta:
        model = SchoolFundPettyCash
        fields = ['id', 'account', 'payee_name', 'cheque_number', 'amount', 'description', 'date_issued', 'school_fund_receipt']
