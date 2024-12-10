from rest_framework import serializers
from .models import PettyCash

class PettyCashSerializer(serializers.ModelSerializer):
    payeeName = serializers.CharField(source='payee_name')
    chequeNumber = serializers.CharField(source='cheque_number')
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    dateIssued = serializers.DateTimeField(source='date_issued')
    account = serializers.CharField()

    class Meta:
        model = PettyCash
        fields = [
            'id', 'account', 'payeeName', 'chequeNumber', 'amount',
            'description', 'dateIssued'
        ]
