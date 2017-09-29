from rest_framework import serializers
from backend.apps.v1.inventory.serializers.AbstractSerializers import ItemSpecificationSerializer
from backend.apps.v1.inventory.serializers.DimensionSerializer import DimensionSerializer


class TelevisionSerializer(ItemSpecificationSerializer):
    dimension = DimensionSerializer()
    tvType = serializers.CharField()
