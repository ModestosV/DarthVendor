from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.Tablet import Tablet

from backend.apps.v1.inventory.serializers.DesktopSerializer import DesktopSerializer
from backend.apps.v1.inventory.serializers.LaptopSerializer import LaptopSerializer
from backend.apps.v1.inventory.serializers.MonitorDisplay import MonitorDisplaySerializer
from backend.apps.v1.inventory.serializers.TabletSerializer import TabletSerializer
from backend.apps.v1.inventory.serializers.ItemIDSerializer import ItemIDSerializer

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper

from backend.apps.v1.accounts.ObjectSession import ObjectSession


class ItemIDsForSpecView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        user = ObjectSession.sessions[request.session['user']]

        modelNumber = request.data['modelNumber']
        type = request.data['type']

        itemIDs = user.itemAdministration.getItemIDs(modelNumber, type)

        serializedItemIDs = list()

        for itemID in itemIDs:
            serializedItemIDs.append(ItemIDSerializer(itemID).data)

        return Response(serializedItemIDs, status=status.HTTP_200_OK)


class DeleteItemID(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        itemSpec = ItemSpecMapper.find(request.data['modelNumber'])
        itemID = ItemIDMapper.findBySerialNum(request.data['serialNumber'], itemSpecification)

        user.itemAdministration.delete(itemID)

        return Response({}, status=status.HTTP_200_OK)
