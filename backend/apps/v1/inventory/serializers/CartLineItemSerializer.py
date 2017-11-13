from rest_framework import serializers
from backend.apps.v1.inventory.serializers.ItemIDSerializer import ItemIDSerializer


class CartLineItemSerializer(serializers.Serializer):

    itemID = serializers.SerializerMethodField()
    additionTime = serializers.DateTimeField()

    def get_itemID(self, cartLineItem):
        return ItemIDSerializer(cartLineItem.itemID).data
