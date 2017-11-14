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
from backend.apps.v1.inventory.serializers.MonitorDisplaySerializer import MonitorDisplaySerializer
from backend.apps.v1.inventory.serializers.TabletSerializer import TabletSerializer
from backend.apps.v1.inventory.serializers.ItemIDSerializer import ItemIDSerializer

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper

from backend.apps.v1.accounts.ObjectSession import ObjectSession


class InitiateEdit(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        print('initiateEdit')

        try:
            user = ObjectSession.sessions[request.session['user']]
            user.itemAdministration.initiateEdit()
            return Response({}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class TerminateEdit(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        print('terminateEdit')
        try:
            user = ObjectSession.sessions[request.session['user']]
            user.itemAdministration.terminateEdit()
            return Response({}, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class CancelEditView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        try:
            user = ObjectSession.sessions[request.session['user']]
            user.itemAdministration.cancelEdit()
            return Response({}, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class AddItemSpecView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        user = ObjectSession.sessions[request.session['user']]
        itemData = request.data
        itemType = itemData["type"]
        item = None
        try:
            if itemType == "Desktop":
                item = Desktop(itemData)
            elif itemType == "Monitor Display":
                item = MonitorDisplay(itemData)
            elif itemType == "Laptop":
                item = Laptop(itemData)
            elif itemType == "Tablet":
                item = Tablet(itemData)
        except Exception as error:
            print(error)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        user.itemAdministration.addItemSpec(item)
        return Response("It Worked")


class ModifyItemSpecView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        user = ObjectSession.sessions[request.session['user']]
        itemData = request.data
        itemType = itemData["type"]
        item = None
        try:
            if itemType == "DESKTOP":
                item = Desktop(itemData)
            elif itemType == "MONITOR":
                item = MonitorDisplay(itemData)
            elif itemType == "LAPTOP":
                item = Laptop(itemData)
            elif itemType == "TABLET":
                item = Tablet(itemData)
        except Exception as error:
            print(error)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        user.itemAdministration.modifyItemSpec(item)
        return Response("It Worked")


class AddQuantityView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        user = ObjectSession.sessions[request.session['user']]

        quantity = request.data['addQuantity']
        modelNumber = request.data['modelNumber']
        type = request.data['type']

        success = user.itemAdministration.addQuantity(modelNumber, type, quantity)
        if success:
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class getEditStateView(APIView):

    def get(self, request):
        user = ObjectSession.sessions[request.session['user']]

        if user.itemAdministration.uow is None:
            return Response({'currentlyEditing': False}, status=status.HTTP_200_OK)
        else:

            serializedNewItems = list()
            for item in user.itemAdministration.uow.newSpecs:
                if isinstance(item, Desktop):
                    item = DesktopSerializer(item).data
                    serializedNewItems.append(item)
                elif isinstance(item, Laptop):
                    item = LaptopSerializer(item).data
                    serializedNewItems.append(item)
                elif isinstance(item, MonitorDisplay):
                    item = MonitorDisplaySerializer(item).data
                    serializedNewItems.append(item)
                elif isinstance(item, Tablet):
                    item = TabletSerializer(item).data
                    serializedNewItems.append(item)

            serializedDirtyItems = list()
            for item in user.itemAdministration.uow.dirtySpecs:
                if isinstance(item, Desktop):
                    item = DesktopSerializer(item).data
                    serializedDirtyItems.append(item)
                elif isinstance(item, Laptop):
                    item = LaptopSerializer(item).data
                    serializedDirtyItems.append(item)
                elif isinstance(item, MonitorDisplay):
                    item = MonitorDisplaySerializer(item).data
                    serializedDirtyItems.append(item)
                elif isinstance(item, Tablet):
                    item = TabletSerializer(item).data
                    serializedDirtyItems.append(item)

            addedItemIDs = user.itemAdministration.uow.newItemIDs
            serializedAddedItemIDs = list()
            for itemID in addedItemIDs:
                serializedAddedItemIDs.append(ItemIDSerializer(itemID).data)

            deletedItemIDs = user.itemAdministration.uow.deletedItemIDs
            serializedDeletedItemIDs = list()
            for itemID in deletedItemIDs:
                serializedDeletedItemIDs.append(ItemIDSerializer(itemID).data)

            return Response({
                'currentlyEditing': True,
                'newSpecs': serializedNewItems,
                'dirtySpecs': serializedDirtyItems,
                'addedItemIDs': serializedAddedItemIDs,
                'deletedItemIDs': serializedDeletedItemIDs
            }, status=status.HTTP_200_OK)
