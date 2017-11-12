from rest_framework import serializers
from backend.utils.database import Database
from .token import TokenSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    password = serializers.HiddenField(default='')
    isAdmin = serializers.BooleanField(default='')


class UserSerializerLogin(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    password = serializers.HiddenField(default='')
    isAdmin = serializers.BooleanField(default='')
