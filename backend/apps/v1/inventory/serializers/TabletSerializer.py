from rest_framework import serializers
from backend.apps.v1.inventory.serializers.AbstractSerializers import AbstractComputerSerializer


class TabletSerializer(AbstractComputerSerializer):
    os = serializers.CharField()
    dx = serializers.FloatField()
    dy = serializers.FloatField()
    dz = serializers.FloatField()
    dimensionFormat = serializers.CharField()
    size = serializers.FloatField()
    sizeFormat = serializers.CharField()
    cameraInfo = serializers.CharField()
    batteryInfo = serializers.CharField()
