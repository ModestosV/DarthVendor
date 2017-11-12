from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.apps.v1.inventory.TDGs.DesktopIDTDG import DesktopIDTDG
from backend.apps.v1.inventory.TDGs.LaptopIDTDG import LaptopIDTDG
from backend.apps.v1.inventory.TDGs.MonitorDisplayIDTDG import MonitorDisplayIDTDG
from backend.apps.v1.inventory.TDGs.TabletIDTDG import TabletIDTDG
from backend.apps.v1.inventory.models.ItemID import ItemID


class ItemIDMapper():

    @staticmethod
    def insert(itemID):

        if (type(itemID.spec) is Desktop):
            result = DesktopIDTDG.insert(itemID)

        elif (type(itemID.spec) is Laptop):
            result = LaptopIDTDG.insert(itemID)

        elif (type(itemID.spec) is MonitorDisplay):
            result = MonitorDisplayIDTDG.insert(itemID)

        elif (type(itemID.spec) is Tablet):
            result = TabletIDTDG.insert(itemID)

        return result

    @staticmethod
    def delete(itemID):

        if (type(itemID.spec) is Desktop):
            DesktopIDTDG.delete(itemID.serialNumber)

        elif (type(itemID.spec) is Laptop):
            LaptopIDTDG.delete(itemID.serialNumber)

        elif (type(itemID.spec) is MonitorDisplay):
            MonitorDisplayIDTDG.delete(itemID.serialNumber)

        elif (type(itemID.spec) is Tablet):
            TabletIDTDG.delete(itemID.serialNumber)

    @staticmethod
    def lock(type, uow):

        if (type == "DESKTOP"):
            result = DesktopIDTDG.lock(uow)

        elif (type == "LAPTOP"):
            result = LaptopIDTDG.lock(uow)

        elif (type == "MONITOR"):
            result = MonitorDisplayIDTDG.lock(uow)

        elif (type == "TABLET"):
            result = TabletIDTDG.lock(uow)

        return result


    @staticmethod
    def unlock(type, uow):
        if (type == "DESKTOP"):
            result = DesktopIDTDG.unlock(uow)

        elif (type == "LAPTOP"):
            result = LaptopIDTDG.unlock(uow)

        elif (type == "MONITOR"):
            result = MonitorDisplayIDTDG.unlock(uow)

        elif (type == "TABLET"):
            result = TabletIDTDG.unlock(uow)

        return result

    @staticmethod
    def find(itemSpecification):

        itemIDList = list()
        result = []
        if(itemSpecification.type == "DESKTOP"):
            result = DesktopIDTDG.findBySpec(itemSpecification)

        elif(itemSpecification.type == "LAPTOP"):
            result = LaptopIDTDG.findBySpec(itemSpecification)

        elif(itemSpecification.type == "MONITOR"):
            result = MonitorDisplayIDTDG.findBySpec(itemSpecification)

        elif(itemSpecification.type == "TABLET"):
            result = TabletIDTDG.findBySpec(itemSpecification)

        for row in result:
            newItemID = ItemID(row.get('serialNum'), row.get('isLocked'), itemSpecification)
            itemIDList.append(newItemID)

        return itemIDList
