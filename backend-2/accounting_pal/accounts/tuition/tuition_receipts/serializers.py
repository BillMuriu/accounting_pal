from rest_framework import serializers
from .models import TuitionReceipt  # Import the TuitionReceipt model

class TuitionReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionReceipt
        fields = [
            'id', 'account', 'received_from',
            'cash_bank', 'total_amount', 'date',
            # 'petty_cash' 
        ]
