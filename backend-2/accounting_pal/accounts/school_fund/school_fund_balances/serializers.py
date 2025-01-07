from rest_framework import serializers
from .models import SchoolFundOpeningBalance  # Updated model for School Fund
from django.utils import timezone

class SchoolFundOpeningBalanceSerializer(serializers.ModelSerializer):
    bankAmount = serializers.DecimalField(max_digits=10, decimal_places=2, source='bank_amount')
    cashAmount = serializers.DecimalField(max_digits=10, decimal_places=2, source='cash_amount')
    date = serializers.DateTimeField()

    class Meta:
        model = SchoolFundOpeningBalance  # Use the new model for school fund
        fields = ['id', 'account', 'date', 'bankAmount', 'cashAmount', 'description']


class RunningSchoolFundBalanceSerializer(serializers.Serializer):
    account = serializers.CharField(max_length=255)
    date = serializers.DateField()
    bankAmount = serializers.DecimalField(max_digits=10, decimal_places=2)
    cashAmount = serializers.DecimalField(max_digits=10, decimal_places=2)


class SchoolFundBalanceCarriedForwardSerializer(serializers.Serializer):
    account = serializers.CharField()
    date = serializers.DateField()
    bankAmount = serializers.DecimalField(max_digits=12, decimal_places=2)
    cashAmount = serializers.DecimalField(max_digits=12, decimal_places=2)
