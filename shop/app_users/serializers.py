from .models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['fullName', 'email', 'phone', 'avatar']


class PasswordSerializer(serializers.ModelSerializer):
    model = CustomUser
    fields = ['password']