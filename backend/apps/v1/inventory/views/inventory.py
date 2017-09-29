from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.serializers.AbstractSerializers import AbstractComputerSerializer, ItemSpecificationSerializer, TestComp

class InventoryView(APIView):

    def get(self, request):
        
        return Response('test')
