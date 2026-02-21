from rest_framework import serializers
from .models import User


class SingUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "created",
            "updated",
            "last_login",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tokens'] = instance.token()
        return data