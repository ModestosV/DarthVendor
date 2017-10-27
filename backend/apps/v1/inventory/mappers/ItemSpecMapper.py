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


class ItemSpecMapper.py:
    
    @staticmethod
    def insert(itemspec):

    
    @staticmethod
    def update(itemspec):
    
    @staticmethod
    def lock(type, uow):
        if(itemspec is Desktop):
            result = DesktopTDG.lock(uow)

        elif(itemspec is Laptop):
            result = LaptopTDG.lock(uow)

        elif(itemspec is MonitorDisplay):
            result = MonitorDisplayTDG.lock(uow)

        elif(itemspec is Tablet):
            result = TabletTDG.lock(uow)
        
        return result
    
    @staticmethod
    def unlock(type):
        
    @staticmethod
    def deleteItem(id):
        if(id.spec is Desktop):
            result = DesktopTDG.find(itemspec.modelNumber)

        elif(id.spec is Laptop):
            result = LaptopTDG.find(itemspec.modelNumber)

        elif(id.spec is MonitorDisplay):
            result = MonitorDisplayTDG.find(itemspec.modelNumber)

        elif(id.spec is Tablet):
            result = TabletTDG.find(itemspec.modelNumber)
        
        return result
        
    @staticmethod
    def find(itemspec):
        if(itemspec is Desktop):
            result = DesktopTDG.find(itemspec.modelNumber)

        elif(itemspec is Laptop):
            result = LaptopTDG.find(itemspec.modelNumber)

        elif(itemspec is MonitorDisplay):
            result = MonitorDisplayTDG.find(itemspec.modelNumber)

        elif(itemspec is Tablet):
            result = TabletTDG.find(itemspec.modelNumber)
        
        return result
    
    @staticmethod
    def findAll(filterlist):
        
        if (filterlist['type'] = "DESKTOP"):
            result = DesktopTDG.find(filterlist)

        elif(filterlist['type'] = "LAPTOP"):
            result = LaptopTDG.find(filterlist)
        
        elif(filterlist['type'] = "TABLET"):
            result = TabletTDG.find(filterlist)
        
        elif(filterlist['type'] = "MONITOR"):
            result = MonitorDisplayTDG.find(filterlist)
        
        for row in result:
            if (filterlist['type'] = "DESKTOP"):
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

            elif(filterlist['type'] = "LAPTOP"):
                result = LaptopTDG.find(filterlist)
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
        
            elif(filterlist['type'] = "TABLET"):
                result = TabletTDG.find(filterlist)
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
        
            elif(filterlist['type'] = "MONITOR"):
                result = MonitorDisplayTDG.find(filterlist)
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
