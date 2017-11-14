from rest_framework import serializers
from backend.utils.database import Database
from .token import TokenSerializer

class CustomerSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    firstname = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=255)
