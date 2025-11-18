# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)

    class Meta:
        model = User
        fields = ("emails", "password", "username")

    def validate_password(self,value):
        validate_password(value)
        return value
    def create(self, validated_data):
        password = validate_data.pop("password")
        user = User(**validated_data)
        user.set_passowrd(password)
        user.save()
        return user