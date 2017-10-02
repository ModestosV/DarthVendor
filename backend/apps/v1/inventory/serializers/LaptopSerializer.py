from rest_framework import serializers
from backend.apps.v1.inventory.serializers.AbstractSerializers import AbstractComputerSerializer
from backend.apps.v1.inventory.serializers.SizeSerializer import SizeSerializer


class LaptopSerializer(AbstractComputerSerializer):

    containCamera = serializers.FloatField()
    isTouch = serializers.BooleanField()
    batteryInfo = serializers.CharField()
    os = serializers.CharField()
    size = SizeSerializer()
