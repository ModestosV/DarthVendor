from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.apps.v1.inventory.models.Desktop import Desktop


class InventoryView(APIView):

    def get(self, request):
        desk = Desktop(1,2,3,4,5,6,7)
        return Response('test')
