from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID
from backend.apps.v1.inventory.models.ItemID import ItemID
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.Purchase import Purchase


class ReturItem(APIView):
    
    def get(self, request):
        purchase = Purchase()
        purchase.returnItems()
       

        return Response()