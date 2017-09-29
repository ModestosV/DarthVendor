from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from backend.apps.v1.inventory.models.Store


class ItemView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):

        itemData = request.data
        itemType = itemData["type"]

        print(itemData)
        item
        try:
            if itemType == "Television":
                dimension = Dimension(itemData["dx"], itemData["dy"], itemData["dz"])
                television = Television(itemData["modelNumber"], itemData["name"], itemData["quantity"], itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"], dimension, itemData["tvType"])
            elif itemType == "Desktop":
                dimension = Dimension(itemData["dx"], itemData["dy"], itemData["dz"])
                desktop = Desktop(itemData["modelNumber"], itemData["name"], itemData["quantity"], itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"], itemData["ramSize"], itemData["ramFormat"], itemData["processorType"], itemData["numCores"], itemData["hardDriveSize"], itemData["hardDriveFormat"], dimension)
            elif itemType == "Monitor Display":
                size = Size(itemData["size"])
                display = MonitorDisplay(itemData["modelNumber"], itemData["name"], itemData["quantity"], itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"])
            elif itemType == "Laptop":
                dimension = Dimension(itemData["dx"], itemData["dy"], itemData["dz"])
                size = Size(itemData["size"])
                laptop = Laptop(itemData["modelNumber"], itemData["name"], itemData["quantity"], itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"], itemData["ramSize"], itemData["ramFormat"], itemData["processorType"], itemData["numCores"], itemData["hardDriveSize"], itemData["hardDriveFormat"], itemData["containCamera"], itemData["isTouch"], itemData["batteryInfo"], itemData["os"], itemData["size"])
            elif itemType == "Tablet":
                size = Size(itemData["size"])
                dimension = Dimension(itemData["dx"], itemData["dy"], itemData["dz"])
                tablet = Tablet(itemData["modelNumber"], itemData["name"], itemData["quantity"], itemData["weight"], itemData["weightFormat"], itemData["price"], itemData["priceFormat"], itemData["brandName"], itemData["ramSize"], itemData["ramFormat"], itemData["processorType"], itemData["numCores"], itemData["hardDriveSize"], itemData["hardDriveFormat"], itemData["os"], dimension, size, itemData["cameraInfo"], itemData["batteryInfo"])
        except Exception as error:
            print(error)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        return Response("test")
