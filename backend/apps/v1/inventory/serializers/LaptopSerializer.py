from rest_framework import serializers
from backend.apps.v1.inventory.serializers.AbstractSerializers import AbstractComputerSerializer


class LaptopSerializer(AbstractComputerSerializer):

    containCamera = serializers.FloatField()
    isTouch = serializers.BooleanField()
    batteryInfo = serializers.CharField()
    os = serializers.CharField()
    size = serializers.FloatField()
    sizeFormat = serializers.CharField()
