from rest_framework import serializers
from .models import CustomUser
from djoser.serializers import UserCreateSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'username', 'password')