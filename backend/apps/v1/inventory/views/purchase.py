from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from backend.apps.v1.inventory.Purchase import Purchase
from backend.apps.v1.accounts.ObjectSession import ObjectSession

from backend.apps.v1.inventory.serializers.CartSerializer import CartSerializer

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper


class CartView(APIView):

    def get(self, request):
        user = ObjectSession.sessions[request.session['user']]

        cart = user.purchaseController.getCart()
        serializedCart = CartSerializer(cart).data
        return Response(serializedCart, status=status.HTTP_200_OK)


class AddToCartView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        user = ObjectSession.sessions[request.session['user']]

        itemSpec = ItemSpecMapper.find(request.data['modelNumber'], request.data['type'])

        user.purchaseController.addItem(itemSpec)

        return Response({}, status=status.HTTP_200_OK)
