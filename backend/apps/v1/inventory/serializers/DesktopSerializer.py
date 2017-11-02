from backend.apps.v1.inventory.serializers.AbstractSerializers import AbstractComputerSerializer
from rest_framework import serializers



class DesktopSerializer(AbstractComputerSerializer):
    dx = serializers.FloatField()
    dy = serializers.FloatField()
    dz = serializers.FloatField()
    dimensionFormat = serializers.CharField()
