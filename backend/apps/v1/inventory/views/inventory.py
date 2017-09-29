from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Dimension import Dimension
from backend.apps.v1.inventory.models.Store import Store
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.Dimension import Dimension
from backend.apps.v1.inventory.serializers.AbstractSerializers import AbstractComputerSerializer, ItemSpecificationSerializer
from backend.apps.v1.inventory.serializers.DimensionSerializer import DimensionSerializer
from backend.apps.v1.inventory.serializers.DesktopSerializer import DesktopSerializer

class InventoryView(APIView):

    def get(self, request):

        store = Store()
        inventory = store.requestInventoryList()
        serializedItems = []

        print(inventory)
        for item in inventory:
            if isinstance(item, Desktop):
                item = DesktopSerializer(item).data
                serializedItems.append(item)
            elif isinstance(item, Laptop):
                item = LaptopSerializer(item).data
                serializedItems.append(item)
            elif isinstance(item, MonitorDisplay):
                item = MonitorDisplaySerializer(item).data
                serializedItems.append(item)
            elif isinstance(item, Tablet):
                item = TabletSerializer(item).data
                serializedItems.append(item)
            elif isinstance(item, Television):
                item = TelevisionSerializer(item)
                serializedItems.append(item)

        return Response(serializedItems)
