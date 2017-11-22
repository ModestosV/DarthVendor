from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Tablet import Tablet

from backend.apps.v1.inventory.models.Catalog import Catalog

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.TDGs.DesktopTDG import DesktopTDG

from backend.apps.v1.inventory.serializers.DesktopSerializer import DesktopSerializer
from backend.apps.v1.inventory.serializers.LaptopSerializer import LaptopSerializer
from backend.apps.v1.inventory.serializers.MonitorDisplaySerializer import MonitorDisplaySerializer
from backend.apps.v1.inventory.serializers.TabletSerializer import TabletSerializer

from backend.apps.v1.accounts.ObjectSession import ObjectSession


class TestView(APIView):

    def get(self, request):
        
        return Response()
