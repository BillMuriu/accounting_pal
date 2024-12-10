# serializers.py
from rest_framework import serializers
from .models import TermPeriod

class TermPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermPeriod
        fields = ['id', 'term_name', 'start_date', 'end_date', 'year', 'fees']
