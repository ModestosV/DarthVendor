from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from backend.apps.v1.inventory.Purchase import Purchase
from backend.apps.v1.accounts.ObjectSession import ObjectSession

from backend.apps.v1.inventory.serializers.CartSerializer import CartSerializer
from backend.apps.v1.inventory.serializers.PurchasedItemIDSerializer import PurchasedItemIDSerializer

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper


class CartView(APIView):

    def get(self, request):
        user = ObjectSession.sessions[request.session['user']]

        cart = user.purchaseController.getCart()
        if cart:
            serializedCart = CartSerializer(cart).data
            return Response(serializedCart, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_200_OK)


class AddToCartView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        user = ObjectSession.sessions[request.session['user']]

        itemSpec = ItemSpecMapper.find(request.data['modelNumber'], request.data['type'])

        user.purchaseController.addItem(itemSpec)

        return Response({}, status=status.HTTP_200_OK)


class RemoveFromCartView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        user = ObjectSession.sessions[request.session['user']]
        itemSpec = ItemSpecMapper.find(request.data['itemID']['itemSpec']['modelNumber'], request.data['itemID']['itemSpec']['type'])
        itemID = ItemIDMapper.findBySerialNumber(request.data['itemID']['serialNumber'], itemSpec)

        user.purchaseController.removeItem(itemID)

        return Response({}, status=status.HTTP_200_OK)


class ConfirmPurchaseView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        user = ObjectSession.sessions[request.session['user']]

        user.purchaseController.confirmPurchase()

        return Response({}, status=status.HTTP_200_OK)


class GetPurchaseCollection(APIView):

    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        user = ObjectSession.sessions[request.session['user']]

        purchaseCollection = user.purchaseController.getPurchaseCollection(user)

        serializedPurchasedItemIDs = list()

        for purchasedItemID in purchaseCollection:
            serializedPurchasedItemIDs.append(PurchasedItemIDSerializer(purchasedItemID).data)

        return Response(serializedPurchasedItemIDs, status=status.HTTP_200_OK)
