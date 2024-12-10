from rest_framework import serializers
from .models import RMIPettyCash

class RMIPettyCashSerializer(serializers.ModelSerializer):
    class Meta:
        model = RMIPettyCash
        fields = ['id', 'account', 'payee_name', 'cheque_number', 'amount', 'description', 'date_issued']
