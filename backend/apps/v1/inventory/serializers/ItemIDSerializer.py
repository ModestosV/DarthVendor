from rest_framework import serializers


class ItemIDSerializer(serializers.Serializer):

    serialNumber = serializers.CharField()
    isLocked = serializers.IntegerField()
    spec = serializers.SerializerMethodField()

    def get_spec(self, itemID):
        return itemID.spec.modelNumber
