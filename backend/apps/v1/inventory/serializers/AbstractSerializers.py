from rest_framework import serializers
from backend.utils.database import Database


class ItemSpecificationSerializer(serializers.Serializer):
    modelNumber = serializers.CharField()
    weight = serializers.FloatField()
    weightFormat = serializers.CharField()
    price = serializers.DecimalField(max_digits=20, decimal_places=2)
    priceFormat = serializers.CharField()
    brandName = serializers.CharField()
    type = serializers.CharField()
    quantity = serializers.SerializerMethodField()

    def get_quantity(self, item):
        with Database() as cursor:
            query = """
                SELECT *
                FROM item
                WHERE modelNumber='{}'
            """.format(item.modelNumber)

            try:
                cursor.execute(query)
                item = cursor.fetchone()
                return item["quantity"]
            except Exception as error:
                print(error)
                return None


class AbstractComputerSerializer(ItemSpecificationSerializer):
    ramSize = serializers.IntegerField()
    ramFormat = serializers.CharField()
    processorType = serializers.CharField()
    numCores = serializers.IntegerField()
    hardDriveSize = serializers.IntegerField()
    hardDriveFormat = serializers.CharField()
