from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Tablet import Tablet

from backend.apps.v1.inventory.serializers.DesktopSerializer import DesktopSerializer
from backend.apps.v1.inventory.serializers.LaptopSerializer import LaptopSerializer
from backend.apps.v1.inventory.serializers.MonitorDisplay import MonitorDisplaySerializer
from backend.apps.v1.inventory.serializers.TabletSerializer import TabletSerializer

from backend.apps.v1.accounts.ObjectSession import ObjectSession


class InventoryView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        user = ObjectSession.sessions[request.session['user']]
        specList = user.itemAdministration.getCatalog()
        serializedItems = []

        for item in specList:
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
        return Response(serializedItems)
