from rest_framework import serializers


class ItemSpecificationSerializer(serializers.Serializer):
    modelNumber = serializers.CharField()
    weight = serializers.FloatField()
    weightFormat = serializers.CharField()
    price = serializers.FloatField()
    priceFormat = serializers.CharField()
    brandName = serializers.CharField()


class AbstractComputerSerializer(ItemSpecificationSerializer):
    ramSize = serializers.IntegerField()
    ramFormat = serializers.CharField()
    processorType = serializers.CharField()
    numCores = serializers.IntegerField()
    hardDriveSize = serializers.IntegerField()
    hardDriveFormat = serializers.CharField()
