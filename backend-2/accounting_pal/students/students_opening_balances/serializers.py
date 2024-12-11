from rest_framework import serializers
from .models import StudentOpeningBalance

class StudentOpeningBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentOpeningBalance
        fields = ['id', 'student', 'balance', 'date_recorded']
