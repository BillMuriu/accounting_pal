from rest_framework import serializers
from .models import RMIBankCharge

class RMIBankChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RMIBankCharge
        fields = ['id', 'account', 'amount', 'charge_date', 'description']
