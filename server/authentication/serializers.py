from rest_framework import serializers
from authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer para o objeto de registro"""
    password = serializers.CharField(
        max_length=28,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    """Serializer para o objeto de usuário"""
    class Meta:
        model = User
        fields = ['id','username','email','created_at','is_staff','is_superuser']