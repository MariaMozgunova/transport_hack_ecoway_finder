from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)

        if validated_data.get('password') is None:
            return instance
        
        password = validated_data.get('password')
        instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        if validated_data.get('password') is None:
            return instance
        
        password = validated_data.get('password')
        instance.set_password(password)
        instance.save()
        return instance


    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "driver_licence",
            "first_name",
            "last_name",
            "date_joined",
            'password',
            'role',
        ]
        extra_kwargs = {
            "date_joined": {"read_only": True},
            'password': {'write_only': True},
        }


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = User.objects.get(username=attrs["username"])
        
        if not user.check_password(attrs["password"]):
            raise ValidationError("No account found with given credentials")
        
        attrs["id"] = user.id
        return attrs

    class Meta:
        model = User
        fields = ["username", "password", "id"]
