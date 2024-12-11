from rest_framework import serializers
from .models import TuitionPettyCash

class TuitionPettyCashSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionPettyCash
        fields = ['id', 'account', 'payee_name', 'cheque_number', 'amount', 'description', 'date_issued']
