from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.v1.inventory.models.Store import Store
from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.apps.v1.inventory.TDGs.DesktopTDG import DesktopTDG

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.ItemAdminUOW import ItemAdminUOW


class ItemView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def get(self, request):

        uow = ItemAdminUOW()
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
        print(uow.registerDirtySpec(desktop1))
        print(uow.registerNewSpec(desktop2))
        uow.commit()
        result = ItemSpecMapper.findAll({'type': 'DESKTOP'})
        print(result)

        return Response()

    def post(self, request):
        store = Store()
        itemData = request.data
        itemType = itemData["type"]
        item = None
        print(itemData)
        try:
            if itemType == "Desktop":
                item = Desktop(
                    itemData["modelNumber"], itemData["name"], itemData["quantity"],
                    itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"],
                    itemData["ramSize"], itemData["ramFormat"], itemData["processorType"], itemData["numCores"],
                    itemData["hardDriveSize"], itemData["hardDriveFormat"], itemData["dx"], itemData["dy"], itemData["dz"]
                )
            elif itemType == "Monitor Display":
                item = MonitorDisplay(
                    itemData["modelNumber"], itemData["name"], itemData["quantity"],
                    itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"], itemData["size"]
                )
            elif itemType == "Laptop":
                item = Laptop(
                    itemData["modelNumber"], itemData["name"], itemData["quantity"],
                    itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"],
                    itemData["ramSize"], itemData["ramFormat"], itemData["processorType"], itemData["numCores"],
                    itemData["hardDriveSize"], itemData["hardDriveFormat"],
                    itemData["containCamera"], itemData["isTouch"], itemData["batteryInfo"], itemData["os"], itemData["size"]
                )
            elif itemType == "Tablet":
                item = Tablet(
                    itemData["modelNumber"], itemData["name"], itemData["quantity"],
                    itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"],
                    itemData["ramSize"], itemData["ramFormat"], itemData["processorType"], itemData["numCores"],
                    itemData["hardDriveSize"], itemData["hardDriveFormat"], itemData["os"], itemData["dx"], itemData["dy"], itemData["dz"],
                    itemData["size"], itemData["cameraInfo"], itemData["batteryInfo"]
                )
        except Exception as error:
            print(error)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        store.confirmItemCreation(item)
        return Response("It Worked")
