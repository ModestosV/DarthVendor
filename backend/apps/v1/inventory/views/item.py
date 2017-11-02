from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.v1.inventory.models.Store import Store
from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.apps.v1.inventory.TDGs.DesktopTDG import DesktopTDG


class ItemView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        self.desktop = Desktop(
            'ZZZZZZd',
            'Razer Desktop',
            46,
            15.0,
            'LBS',
            2299.99,
            'CAD',
            'RAZER',
            16,
            'GB',
            'INTEL',
            4,
            2,
            'TB',
            15,
            30,
            1,
            'INCH'
        )
        DesktopTDG.insert(self.desktop)
        result = DesktopTDG.find(self.desktop.modelNumber)
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
