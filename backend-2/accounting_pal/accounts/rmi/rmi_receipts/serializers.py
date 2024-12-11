from rest_framework import serializers
from .models import RMIReceipt

class RMIReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = RMIReceipt
        fields = [
            'id', 'account', 'received_from', 
            'cash_bank', 'total_amount', 'date'
        ]
