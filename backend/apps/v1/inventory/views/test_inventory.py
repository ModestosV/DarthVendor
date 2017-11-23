from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Tablet import Tablet

from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification
from backend.apps.v1.inventory.models.CartLineItem import CartLineItem
from backend.apps.v1.inventory.models.ItemID import ItemID
from backend.apps.v1.inventory.models.PurchaseCollection import PurchaseCollection
from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID
from backend.apps.v1.inventory.models.Cart import Cart

from backend.apps.v1.inventory.models.Catalog import Catalog

from backend.apps.v1.accounts.ObjectSession import ObjectSession

from backend.apps.v1.inventory.TDGs.DesktopIDTDG import DesktopIDTDG
from backend.apps.v1.inventory.TDGs.LaptopIDTDG import LaptopIDTDG
from backend.apps.v1.inventory.TDGs.TabletIDTDG import TabletIDTDG
from backend.apps.v1.inventory.TDGs.MonitorDisplayIDTDG import MonitorDisplayIDTDG
from backend.apps.v1.inventory.TDGs.PurchasedItemIDTDG import PurchasedItemIDTDG
from backend.apps.v1.inventory.TDGs.DesktopTDG import DesktopTDG
from backend.apps.v1.inventory.TDGs.LaptopTDG import LaptopTDG
from backend.apps.v1.inventory.TDGs.TabletTDG import TabletTDG
from backend.apps.v1.inventory.TDGs.MonitorDisplayTDG import MonitorDisplayTDG


class InventoryTestView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):

        """result = DesktopTDG.find("VR7RC")

        if(not result):
            print("found nothing")
        else:
            for row in result:
                print(row)"""

        """result = DesktopTDG.findAll()

        if(not result):
            print("found nothing")
        else:
            for row in result:
                print(row)"""

        """spec = ItemSpecification("1111AAA","jane",0,0,"",0,"","","")"""

        """desktop = Desktop({
            'modelNumber': "1111AAA",
            'name': "jane",
            'quantity': 0,
            'weight': 0,
            'weightFormat': "",
            'price': 0,
            'priceFormat': "",
            'brandName': "",
            'ramSize': 0,
            'ramFormat': "",
            'processorType': "",
            'numCores': 0,
            'hardDriveSize': 0,
            'hardDriveFormat': "",
            'dx': 0,
            'dy': 0,
            'dz': 0})"""
        """DesktopTDG.insert(desktop)"""
        """desktop = Desktop({
            'modelNumber': "19999",
            'name': "jane",
            'quantity': 0,
            'weight': 40,
            'weightFormat': "",
            'price': 0,
            'priceFormat': "",
            'brandName': "",
            'ramSize': 0,
            'ramFormat': "",
            'processorType': "",
            'numCores': 0,
            'hardDriveSize': 0,
            'hardDriveFormat': "",
            'dx': 0,
            'dy': 0,
            'dz': 0})
        DesktopTDG.update(desktop)"""

       
        return Response()
