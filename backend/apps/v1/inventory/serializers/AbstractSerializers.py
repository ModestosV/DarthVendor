from rest_framework import serializers
from backend.apps.v1.inventory.models.Catalog import Catalog


class ItemSpecificationSerializer(serializers.Serializer):
    modelNumber = serializers.CharField()
    name = serializers.CharField()
    brandName = serializers.CharField()
    price = serializers.DecimalField(max_digits=20, decimal_places=2)
    weight = serializers.FloatField()
    weightFormat = serializers.CharField()
    priceFormat = serializers.CharField()
    type = serializers.CharField()
    # quantity = serializers.HiddenField(default='')
    quantity = serializers.SerializerMethodField()

    def get_quantity(self, itemSpec):
        """ Get quantity from catalog. """
        return Catalog.getQuantityOfSpec(itemSpec.modelNumber, itemSpec.type)


class AbstractComputerSerializer(ItemSpecificationSerializer):
    ramSize = serializers.IntegerField()
    ramFormat = serializers.CharField()
    processorType = serializers.CharField()
    numCores = serializers.IntegerField()
    hardDriveSize = serializers.IntegerField()
    hardDriveFormat = serializers.CharField()
