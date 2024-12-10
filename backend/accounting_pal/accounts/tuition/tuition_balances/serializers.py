from rest_framework import serializers
from .models import TuitionOpeningBalance

class TuitionOpeningBalanceSerializer(serializers.ModelSerializer):
    bankAmount = serializers.DecimalField(max_digits=10, decimal_places=2, source='bank_amount')
    cashAmount = serializers.DecimalField(max_digits=10, decimal_places=2, source='cash_amount')
    date = serializers.DateTimeField()

    class Meta:
        model = TuitionOpeningBalance
        fields = ['id', 'account', 'date', 'bankAmount', 'cashAmount', 'description']


class TuitionRunningBalanceSerializer(serializers.Serializer):
    account = serializers.CharField(max_length=255)
    date = serializers.DateField()
    bankAmount = serializers.DecimalField(max_digits=10, decimal_places=2)
    cashAmount = serializers.DecimalField(max_digits=10, decimal_places=2)
    

class TuitionBalanceCarriedForwardSerializer(serializers.Serializer):
    account = serializers.CharField()
    date = serializers.DateField()
    bankAmount = serializers.DecimalField(max_digits=12, decimal_places=2)
    cashAmount = serializers.DecimalField(max_digits=12, decimal_places=2)
