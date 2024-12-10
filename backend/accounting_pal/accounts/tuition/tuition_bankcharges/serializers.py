from rest_framework import serializers
from .models import TuitionBankCharge

class TuitionBankChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionBankCharge
        fields = ['id', 'account', 'amount', 'charge_date', 'description']
