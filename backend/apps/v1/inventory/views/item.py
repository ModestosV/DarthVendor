from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.apps.v1.inventory.TDGs.DesktopTDG import DesktopTDG

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper

from backend.apps.v1.inventory.ItemAdminUOW import ItemAdminUOW

from backend.apps.v1.inventory.ItemAdministration import ItemAdministration
from backend.apps.v1.accounts.ObjectSession import ObjectSession


class InitiateEdit(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        print('initiateEdit')

        # try:
        print(ObjectSession.sessions)
        itemAdministration = ObjectSession.sessions[request.session['token']]
        itemAdministration.initiateEdit()
        return Response({}, status=status.HTTP_200_OK)
        # except Exception as error:
        #     print(error)
        #     return Response({}, status=status.HTTP_400_BAD_REQUEST)


class TerminateEdit(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        print('terminateEdit')
        try:
            itemAdministration = ObjectSession.sessions[request.session['token']]
            itemAdministration.terminateEdit()
            return Response({}, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class AddItemSpecView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        print(request.session['userID'])
        try:
            request.session['count'] += 1
        except:
            request.session['count'] = 0

        print(request.session['count'])
        itemAdmin = ItemAdministration()
        desktop1 = Desktop({
            'modelNumber': 'ZZZZZZT',
            'name': 'Razer Desktop',
            'quantity': 46,
            'weight': 15.0,
            'weightFormat': 'LBS',
            'price': 2299.99,
            'priceFormat': 'CAD',
            'brandName': 'RAZER',
            'ramSize': 16,
            'ramFormat': 'GB',
            'processorType': 'DELL',
            'numCores': 4,
            'hardDriveSize': 2,
            'hardDriveFormat': 'GB',
            'dx': 15,
            'dy': 30,
            'dz': 1
        })
        desktop2 = Desktop({
            'modelNumber': 'ZZZZZZW',
            'name': 'Razer Desktop',
            'quantity': 46,
            'weight': 15.0,
            'weightFormat': 'LBS',
            'price': 2299.99,
            'priceFormat': 'CAD',
            'brandName': 'RAZER',
            'ramSize': 16,
            'ramFormat': 'GB',
            'processorType': 'DELL',
            'numCores': 4,
            'hardDriveSize': 2,
            'hardDriveFormat': 'TB',
            'dx': 15,
            'dy': 30,
            'dz': 1
        })

        itemAdmin.initiateEdit()
        itemAdmin.addQuantity(desktop2.modelNumber, "DESKTOP", 5)
        itemAdmin.terminateEdit()
        result = ItemIDMapper.find(desktop2)

        print(len(result))

        return Response()

    def post(self, request):
        print(ObjectSession.sessions)
        itemAdministration = ObjectSession.sessions[request.session['token']]
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

        itemAdministration.addItemSpec(item)
        return Response("It Worked")


class ModifyItemSpecView(APIView):

    def post(self, request):
        itemAdministration = ObjectSession.sessions[request.session['token']]
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

        itemAdministration.modifyItemSpec(item)
        return Response("It Worked")


class getEditStateView(APIView):

    def get(self, request):
        itemAdministration = ObjectSession.sessions[request.session['token']]

        if itemAdministration.uow is None:
            return Response({''})
