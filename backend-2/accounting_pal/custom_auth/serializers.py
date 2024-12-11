from rest_framework import serializers
from .models import CustomUser  # Update to CustomUser model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'role', 'phone_number', 'is_verified']
