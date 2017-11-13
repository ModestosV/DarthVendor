from rest_framework import serializers
from backend.utils.database import Database


class ItemSpecificationSerializer(serializers.Serializer):
    modelNumber = serializers.CharField()
    name = serializers.CharField()
    brandName = serializers.CharField()
    price = serializers.DecimalField(max_digits=20, decimal_places=2)
    weight = serializers.FloatField()
    weightFormat = serializers.CharField()
    priceFormat = serializers.CharField()
    type = serializers.CharField()
    quantity = serializers.IntegerField()



class AbstractComputerSerializer(ItemSpecificationSerializer):
    ramSize = serializers.IntegerField()
    ramFormat = serializers.CharField()
    processorType = serializers.CharField()
    numCores = serializers.IntegerField()
    hardDriveSize = serializers.IntegerField()
    hardDriveFormat = serializers.CharField()
