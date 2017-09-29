from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification
from rest_framework import serializers


class DimensionSerializer(serializers.Serializer):

    x = serializers.IntegerField()
    y = serializers.IntegerField()
    format = serializers.CharField()
    z = serializers.IntegerField()