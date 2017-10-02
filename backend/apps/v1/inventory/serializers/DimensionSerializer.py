from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification
from rest_framework import serializers


class DimensionSerializer(serializers.Serializer):

    x = serializers.FloatField()
    y = serializers.FloatField()
    z = serializers.FloatField()
    format = serializers.CharField()
    