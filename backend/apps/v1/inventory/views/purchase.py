from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from backend.apps.v1.inventory.Purchase import Purchase
from backend.apps.v1.accounts.ObjectSession import ObjectSession

class CartView(APIView):


    def get(self, request):
        return
