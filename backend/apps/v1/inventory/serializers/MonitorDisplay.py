from rest_framework import serializers
from backend.apps.v1.inventory.serializers.AbstractSerializers import ItemSpecificationSerializer
from rest_framework import serializers


class MonitorDisplaySerializer(ItemSpecificationSerializer):
    size = serializers.FloatField()
    sizeFormat = serializers.CharField()
