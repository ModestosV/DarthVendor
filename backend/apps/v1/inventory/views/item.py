from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.v1.inventory.models.Store import Store
from backend.apps.v1.inventory.models.Television import Television
from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.apps.v1.inventory.models.Dimension import Dimension
from backend.apps.v1.inventory.models.Size import Size


class ItemView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        store = Store()
        itemData = request.data
        itemType = itemData["type"]
        item = None
        print(itemData)
        try:
            if itemType == "Television":
                dimension = Dimension(itemData["dx"], itemData["dy"], itemData["dz"])
                item = Television(itemData["modelNumber"], itemData["name"], itemData["quantity"], itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"], dimension, itemData["tvType"])
            elif itemType == "Desktop":
                dimension = Dimension(itemData["dx"], itemData["dy"], itemData["dz"])
                item = Desktop(itemData["modelNumber"], itemData["name"], itemData["quantity"], itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"], itemData["ramSize"], itemData["ramFormat"], itemData["processorType"], itemData["numCores"], itemData["hardDriveSize"], itemData["hardDriveFormat"], dimension)
            elif itemType == "Monitor Display":
                size = Size(itemData["size"])
                item = MonitorDisplay(itemData["modelNumber"], itemData["name"], itemData["quantity"], itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"], size)
            elif itemType == "Laptop":
                dimension = Dimension(itemData["dx"], itemData["dy"], itemData["dz"])
                size = Size(itemData["size"])
                item = Laptop(itemData["modelNumber"], itemData["name"], itemData["quantity"], itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"], itemData["ramSize"], itemData["ramFormat"], itemData["processorType"], itemData["numCores"], itemData["hardDriveSize"], itemData["hardDriveFormat"], itemData["containCamera"], itemData["isTouch"], itemData["batteryInfo"], itemData["os"], itemData["size"])
            elif itemType == "Tablet":
                size = Size(itemData["size"])
                dimension = Dimension(itemData["dx"], itemData["dy"], itemData["dz"])
                item = Tablet(itemData["modelNumber"], itemData["name"], itemData["quantity"], itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"], itemData["ramSize"], itemData["ramFormat"], itemData["processorType"], itemData["numCores"], itemData["hardDriveSize"], itemData["hardDriveFormat"], itemData["os"], dimension, size, itemData["cameraInfo"], itemData["batteryInfo"])
        except Exception as error:
            print(error)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        store.confirmItemCreation(item)
        return Response("It Worked")
