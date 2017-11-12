from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper

from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.apps.v1.inventory.TDGs.DesktopIDTDG import DesktopIDTDG
from backend.apps.v1.inventory.TDGs.LaptopIDTDG import LaptopIDTDG
from backend.apps.v1.inventory.TDGs.MonitorDisplayIDTDG import MonitorDisplayIDTDG
from backend.apps.v1.inventory.TDGs.TabletIDTDG import TabletIDTDG
from backend.apps.v1.inventory.models.ItemID import ItemID


class Catalog:

    def __init__(self, params):
        specs = Catalog.getAllSpecs()

    @staticmethod
    def getAllSpecs():
        types = ["MONITOR", "DESKTOP", "TABLET", "LAPTOP"]
        specs = list()
        for specType in types:
            specs += ItemSpecMapper.findAll({'type': specType})
        return specs

    #should take in list of ItemId Objects to update the catalog with
    #this is from an action like a customer purchasing items
    @staticmethod
    def updateCatalog(itemsChanged, uow):
        itemsNoLongerAvailable = list()
        for item in itemsChanged:
            if item is not None:
                # checks if the items in the list of items to update in DB and Catalog
                if (ItemIDMapper.lock(item.spec.type)):
                    ItemIDMapper.delete(item)
                    ItemIDMapper.unlock(item.spec.type)
                    item = None
                    #should then indicate the success of the item being
                else:
                    itemsNoLongerAvailable.append(ItemID(item.serialNumber, False, item.spec))
                    #should then make sure to constantly try to unlock item of that ItemId as soon as table is unlocked
                    item = None
                    #item should now be removed from cart