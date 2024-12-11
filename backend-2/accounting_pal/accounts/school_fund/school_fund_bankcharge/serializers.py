from rest_framework import serializers
from .models import SchoolFundBankCharges

class SchoolFundBankChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolFundBankCharges
        fields = ['id', 'account', 'amount', 'charge_date', 'description']
