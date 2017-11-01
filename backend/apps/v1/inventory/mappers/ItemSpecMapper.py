from backend.utils.database import Database
from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Dimension import Dimension
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Size import Size
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
    def unlock(type):
        if(type == "DESKTOP"):
            result = DesktopTDG.unlock()

        elif(type == "LAPTOP"):
            result = LaptopTDG.unlock()

        elif(type == "MONITOR"):
            result = MonitorDisplayTDG.unlock()

        elif(type == "TABLET"):
            result = TabletTDG.unlock()

        return result
        
        
    @staticmethod
    def find(itemspec):
        if(type(itemspec) is Desktop):
            result = DesktopTDG.find(itemspec.modelNumber)

        elif(type(itemspec) is Laptop):
            result = LaptopTDG.find(itemspec.modelNumber)

        elif(type(itemspec) is MonitorDisplay):
            result = MonitorDisplayTDG.find(itemspec.modelNumber)

        elif(type(itemspec) is Tablet):
            result = TabletTDG.find(itemspec.modelNumber)
        return result

    @staticmethod
    def findAll(filterlist):
        
        if (filterlist['type'] == "DESKTOP"):
            result = DesktopTDG.find(filterlist)

        elif(filterlist['type'] == "LAPTOP"):
            result = LaptopTDG.find(filterlist)
        
        elif(filterlist['type'] == "TABLET"):
            result = TabletTDG.find(filterlist)
        
        elif(filterlist['type'] == "MONITOR"):
            result = MonitorDisplayTDG.find(filterlist)
        
        itemSpecList = list()

        for row in result:
            if (filterlist['type'] == "DESKTOP"):
                item = Desktop(
                            row.get('modelNumber'),
                            row.get('name'),
                            row.get('quantity'),
                            row.get('weight'),
                            row.get('weightFormat'),
                            row.get('price'),
                            row.get('priceFormat'),
                            row.get('brandName'),
                            row.get('ramSize'),
                            row.get('ramFormat'),
                            row.get('processorType'),
                            row.get('numCores'),
                            row.get('hardDriveSize'),
                            row.get('hardDriveFormat'),
                            Dimension(
                                row.get('dx'),
                                row.get('dy'),
                                row.get('dz'),
                                row.get('dimensionFormat'),
                            ),
                        )
                qty = DesktopIDTDG.getQuantity(item.modelNumber)
                    

            elif(filterlist['type'] == "LAPTOP"):
                item = Laptop(
                            row.get('modelNumber'),
                            row.get('name'),
                            row.get('quantity'),
                            row.get('weight'),
                            row.get('weightFormat'),
                            row.get('price'),
                            row.get('priceFormat'),
                            row.get('brandName'),
                            row.get('ramSize'),
                            row.get('ramFormat'),
                            row.get('processorType'),
                            row.get('numCores'),
                            row.get('hardDriveSize'),
                            row.get('hardDriveFormat'),
                            row.get('containsCamera'),
                            row.get('isTouch'),
                            row.get('batteryInfo'),
                            row.get('os'),
                            Size(
                                row.get('size'), 
                                row.get('sizeFormat')
                            )                            
                        )
                qty = LaptopIDTDG.getQuantity(item.modelNumber)
        
            elif(filterlist['type'] == "TABLET"):
                item = Tablet(
                            row.get('modelNumber'),
                            row.get('name'),
                            row.get('quantity'),
                            row.get('weight'),
                            row.get('weightFormat'),
                            row.get('price'),
                            row.get('priceFormat'),
                            row.get('brandName'),
                            row.get('ramSize'),
                            row.get('ramFormat'),
                            row.get('processorType'),
                            row.get('numCores'),
                            row.get('hardDriveSize'),
                            row.get('hardDriveFormat'),
                            row.get('os'),
                            Dimension(
                                row.get('dx'),
                                row.get('dy'),
                                row.get('dz'),
                                row.get('dimensionFormat'),
                            ),
                            Size(
                                row.get('size'),
                                row.get('sizeFormat')
                            ),
                            row.get('cameraInfo'),
                            row.get('batteryInfo')
                        )
                qty = TabletIDTDG.getQuantity(item.modelNumber)
        
            elif(filterlist['type'] == "MONITOR"):
                item = MonitorDisplay(
                            row.get('modelNumber'), 
                            row.get('name'), 
                            row.get('quantity'),                             
                            row.get('weight'),
                            row.get('weightFormat'), 
                            row.get('price'), 
                            row.get('priceFormat'), 
                            row.get('brandName'), 
                            Size(
                                row.get('size'), 
                                row.get('sizeFormat')
                            )
                        )
                qty = MonitorDisplayIDTDG.getQuantity(item.modelNumber)
            
            itemSpecList.append(item)

        return itemSpecList, qty
