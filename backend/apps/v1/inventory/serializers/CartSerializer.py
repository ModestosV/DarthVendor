from rest_framework import serializers
from backend.apps.v1.inventory.serializers.CartLineItemSerializer import CartLineItemSerializer


class CartSerializer(serializers.Serializer):
    cartItems = CartLineItemSerializer(many=True)
