from backend.utils.database import Database
from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.apps.v1.inventory.TDGs.DesktopTDG import DesktopTDG
from backend.apps.v1.inventory.TDGs.LaptopTDG import LaptopTDG
from backend.apps.v1.inventory.TDGs.MonitorDisplayTDG import MonitorDisplayTDG
from backend.apps.v1.inventory.TDGs.TabletTDG import TabletTDG
from backend.apps.v1.inventory.TDGs.DesktopIDTDG import DesktopIDTDG
from backend.apps.v1.inventory.TDGs.LaptopIDTDG import LaptopIDTDG
from backend.apps.v1.inventory.TDGs.MonitorDisplayIDTDG import MonitorDisplayIDTDG
from backend.apps.v1.inventory.TDGs.TabletIDTDG import TabletIDTDG


class ItemSpecMapper():

    @staticmethod
    def insert(itemspec):
        if(type(itemspec) is Desktop):
            result = DesktopTDG.insert(itemspec)

        elif(type(itemspec) is Laptop):
            result = LaptopTDG.insert(itemspec)

        elif(type(itemspec) is MonitorDisplay):
            result = MonitorDisplayTDG.insert(itemspec)

        elif(type(itemspec) is Tablet):
            result = TabletTDG.insert(itemspec)

        return result

    @staticmethod
    def update(itemspec):
        if(type(itemspec) is Desktop):
            result = DesktopTDG.update(itemspec)

        elif(type(itemspec) is Laptop):
            result = LaptopTDG.update(itemspec)

        elif(type(itemspec) is MonitorDisplay):
            result = MonitorDisplayTDG.update(itemspec)

        elif(type(itemspec) is Tablet):
            result = TabletTDG.update(itemspec)

        return result

    @staticmethod
    def lock(type, uow):

        print(type)
        if(type == "DESKTOP"):
            result = DesktopTDG.lock(uow)

        elif(type == "LAPTOP"):
            result = LaptopTDG.lock(uow)

        elif(type == "MONITOR"):
            result = MonitorDisplayTDG.lock(uow)

        elif(type == "TABLET"):
            result = TabletTDG.lock(uow)

        return result

    @staticmethod
    def unlock(type, uow):
        if(type == "DESKTOP"):
            result = DesktopTDG.unlock(uow)

        elif(type == "LAPTOP"):
            result = LaptopTDG.unlock(uow)

        elif(type == "MONITOR"):
            result = MonitorDisplayTDG.unlock(uow)

        elif(type == "TABLET"):
            result = TabletTDG.unlock(uow)

        return result

    @staticmethod
    def find(modelNumber, specType):
        result = []

        if(specType == "DESKTOP"):
            result = DesktopTDG.find(modelNumber)

        elif(specType == "LAPTOP"):
            result = LaptopTDG.find(modelNumber)

        elif(specType == "MONITOR"):
            result = MonitorDisplayTDG.find(modelNumber)

        elif(specType == "TABLET"):
            result = TabletTDG.find(modelNumber)

        spec = ItemSpecMapper.resultSetToItemSpec([result], specType)
        if len(spec) == 0:
            return None
        else:
            return spec[0]

    @staticmethod
    def findAll(filterlist):

        if (filterlist['type'] == "DESKTOP"):
            result = DesktopTDG.findAll()

        elif(filterlist['type'] == "LAPTOP"):
            result = LaptopTDG.findAll()

        elif(filterlist['type'] == "TABLET"):
            result = TabletTDG.findAll()

        elif(filterlist['type'] == "MONITOR"):
            result = MonitorDisplayTDG.findAll()

        itemSpecList = ItemSpecMapper.resultSetToItemSpec(result, filterlist['type'])
        return itemSpecList

    @staticmethod
    def resultSetToItemSpec(result, specType):
        itemSpecList = list()
        for row in result:
            if row is None:
                break
            elif (specType == "DESKTOP"):
                item = Desktop({
                    'modelNumber': row.get('modelNumber'),
                    'name': row.get('name'),
                    'quantity': row.get('quantity'),
                    'weight': row.get('weight'),
                    'weightFormat': row.get('weightFormat'),
                    'price': row.get('price'),
                    'priceFormat': row.get('priceFormat'),
                    'brandName': row.get('brandName'),
                    'ramSize': row.get('ramSize'),
                    'ramFormat': row.get('ramFormat'),
                    'processorType': row.get('processorType'),
                    'numCores': row.get('numCores'),
                    'hardDriveSize': row.get('hardDriveSize'),
                    'hardDriveFormat': row.get('hardDriveFormat'),
                    'dx': row.get('dx'),
                    'dy': row.get('dy'),
                    'dz': row.get('dz'),
                })

            elif(specType == "LAPTOP"):
                item = Laptop({
                    'modelNumber': row.get('modelNumber'),
                    'name': row.get('name'),
                    'quantity': row.get('quantity'),
                    'weight': row.get('weight'),
                    'weightFormat': row.get('weightFormat'),
                    'price': row.get('price'),
                    'priceFormat': row.get('priceFormat'),
                    'brandName': row.get('brandName'),
                    'ramSize': row.get('ramSize'),
                    'ramFormat': row.get('ramFormat'),
                    'processorType': row.get('processorType'),
                    'numCores': row.get('numCores'),
                    'hardDriveSize': row.get('hardDriveSize'),
                    'hardDriveFormat': row.get('hardDriveFormat'),
                    'containsCamera': row.get('containsCamera'),
                    'isTouch': row.get('isTouch'),
                    'batteryInfo': row.get('batteryInfo'),
                    'os': row.get('os'),
                    'size': row.get('size')
                })

            elif(specType == "TABLET"):
                item = Tablet({
                    'modelNumber': row.get('modelNumber'),
                    'name': row.get('name'),
                    'quantity': row.get('quantity'),
                    'weight': row.get('weight'),
                    'weightFormat': row.get('weightFormat'),
                    'price': row.get('price'),
                    'priceFormat': row.get('priceFormat'),
                    'brandName': row.get('brandName'),
                    'ramSize': row.get('ramSize'),
                    'ramFormat': row.get('ramFormat'),
                    'processorType': row.get('processorType'),
                    'numCores': row.get('numCores'),
                    'hardDriveSize': row.get('hardDriveSize'),
                    'hardDriveFormat': row.get('hardDriveFormat'),
                    'os': row.get('os'),
                    'dx': row.get('dx'),
                    'dy': row.get('dy'),
                    'dz': row.get('dz'),
                    'size': row.get('size'),
                    'cameraInfo': row.get('cameraInfo'),
                    'batteryInfo': row.get('batteryInfo')
                })

            elif(specType == "MONITOR"):
                item = MonitorDisplay({
                    'modelNumber': row.get('modelNumber'),
                    'name': row.get('name'),
                    'quantity': row.get('quantity'),
                    'weight': row.get('weight'),
                    'weightFormat': row.get('weightFormat'),
                    'price': row.get('price'),
                    'priceFormat': row.get('priceFormat'),
                    'brandName': row.get('brandName'),
                    'size': row.get('size')
                })

            itemSpecList.append(item)
        return itemSpecList
