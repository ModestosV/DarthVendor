from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Dimension import Dimension
from backend.apps.v1.inventory.serializers.AbstractSerializers import AbstractComputerSerializer, ItemSpecificationSerializer
from backend.apps.v1.inventory.serializers.DimensionSerializer import DimensionSerializer
from backend.apps.v1.inventory.serializers.DesktopSerializer import DesktopSerializer

class InventoryView(APIView):

    def get(self, request):
        dimension = Dimension(1,2,3,"cm")
        desktop = Desktop(1,2,3,4.5,5,6,7,8,9,10 ,11, 12, dimension)
        serializer = DesktopSerializer(desktop)

        print(serializer.data)
        return Response(serializer.data)
