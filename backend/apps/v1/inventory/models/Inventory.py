from django.conf import settings
from sqlite3 import dbapi2 as Database

from backend.apps.v1.inventory.models.Size import Size
from backend.apps.v1.inventory.models.Dimension import Dimension

from backend.apps.v1.inventory.models.Television import Television
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Desktop import Desktop


class Inventory(object):
    """Constructor"""
    def __init__(self):
        pass
	
    def addItem(self, itemSpec):

        #connection = Database.connect(settings.DATABASES['default']['NAME'])
        connection = Database.connect("/home/andres/venv/darthvendor/SOEN343_GroupProject/backend/db.sqlite3")

        cursor = connection.cursor()

        
        if type(itemSpec) is Laptop:
            if itemSpec.isTouch == True:
                touch = 1
            else:
                touch = 0
            if itemSpec.containCamera == True:
                cam = 1
            else:
                cam = 0
            query1 = self.generateItemQuery("LAPTOP",itemSpec.modelNumber,itemSpec.name, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSpec.price, itemSpec.priceFormat, itemSpec.brandName)
            query2 = """
                INSERT INTO laptop (modelNumber,
                                    ramSize, 
                                    ramFormat, 
                                    processorType, 
                                    numCores, 
                                    hardDriveSize,
                                    hardDriveFormat,
                                    containsCamera, 
                                    isTouch,
                                    batteryInfo,
                                    os,
                                    size,
                                    sizeFormat)
                    VALUES(
                    '{}',
                     {},
                    '{}',
                    '{}',
                     {},
                     {},
                    '{}',
                     {},
                     {},
                    '{}',
                    '{}',
                     {},
                    '{}'
                );
            """.format(itemSpec.modelNumber, itemSpec.ramSize, itemSpec.ramFormat, itemSpec.processorType, itemSpec.numCores, itemSpec.hardDriveSize, itemSpec.hardDriveFormat, cam, touch, itemSpec.batteryInfo, itemSpec.os, itemSpec.size.size, itemSpec.size.sizeFormat)
            print(query1)
            print(query2)
        elif type(itemSpec) is Desktop:
            query1 = generateItemQuery("DESKTOP",itemSpec.modelNumber, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSPec.price, itemSpec.priceFormat, itemSpec.brandName)
            query2 = """
                INSERT INTO desktop (modelNumber,
                                     ramSize, 
                                     ramFormat, 
                                     processorType, 
                                     numCores, 
                                     hardDriveSize,
                                     hardDriveFormat,
                                     dx,
                                     dy,
                                     dz,
                                     dimensionFormat)
                    VALUES(
                    '{}',
                     {},
                    '{}',
                    '{}',
                     {},
                     {},
                    '{}',
                     {},
                     {},
                     {},
                    '{}'
                );
            """.format(itemSpec.ramSize, itemSpec.ramFormat, itemSpec.processorType, itemSpec.numCores, itemSpec.hardDriveSize, itemSpec.hardDriveFormat, itemSpec.dx, itemSpec.dy, itemSpec.dz, itemSpec.dimensionFormat)


        elif type(itemSpec) is MonitorDisplay:

            query1 = self.generateItemQuery("MONITOR",itemSpec.modelNumber,itemSpec.name, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSpec.price, itemSpec.priceFormat, itemSpec.brandName)

            query2 = """
                INSERT INTO monitorDisplay (modelNumber,size, sizeFormat)
                    VALUES(
                     '{}',
                    {},
                    '{}'
                );
            """.format(itemSpec.modelNumber, itemSpec.size.size, itemSpec.size.sizeFormat)
            print(query1)
            print(query2)

        elif type(itemSpec) is Television:
            query1 = self.generateItemQuery("TV",itemSpec.modelNumber,itemSpec.name, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSPec.price, itemSpec.priceFormat, itemSpec.brandName)
            query2 = """
                INSERT INTO television (modelNumber,
                                        tvType, 
                                        dimensionFormat,
                                        dx,
                                        dy,
                                        dz)
                    VALUES(
                    '{}',
                    '{}',
                    '{}',
                     {},
                     {},
                     {}
                );
            """.format(itemSpec.tvType, itemSpec.dimensionFormat, itemSpec.dx, itemSpec.dy, itemSpec.dz)

        elif type(itemSpec) is Tablet:
            query1 = self.generateItemQuery("TABLET",itemSpec.modelNumber,itemSpec.name, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSpec.price, itemSpec.priceFormat, itemSpec.brandName)
            print(query1)
            query2 = """
                INSERT INTO tablet (modelNumber,
                                    ramSize, 
                                    ramFormat, 
                                    processorType, 
                                    numCores, 
                                    hardDriveSize,
                                    hardDriveFormat,
                                    cameraInfo, 
                                    batteryInfo,
                                    os,
                                    size,
                                    sizeFormat,
                                    dx,
                                    dy,
                                    dz,
                                    dimensionFormat)
                    VALUES(
                    '{}',
                     {},
                    '{}',
                    '{}',
                     {},
                     {},
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                     {},
                    '{}',
                     {},
                     {},
                     {},
                    '{}'
                );
            """.format(itemSpec.modelNumber, itemSpec.ramSize, itemSpec.ramFormat, itemSpec.processorType, itemSpec.numCores, itemSpec.hardDriveSize, itemSpec.hardDriveFormat, itemSpec.cameraInfo, itemSpec.batteryInfo, itemSpec.os, itemSpec.size.size, itemSpec.size.sizeFormat, itemSpec.dimension.x, itemSpec.dimension.y, itemSpec.dimension.z, itemSpec.dimension.format)
            print(query2)
        try:
            cursor.execute(query1)
            cursor.execute(query2)
        except Exception as error: 
            print(error)  

        connection.commit()
        connection.close()

    def requestInventoryList(self):
        connection = Database.connect(settings.DATABASES['default']['NAME'])

        cursor = connection.cursor()

        result = []

        queryTablet = """
                SELECT * FROM item, tablet 
                WHERE item.type = "TABLET" 
                AND item.modelNumber = tablet.modelNumber;
        """
        queryTv = """
                SELECT * from item, television 
                WHERE item.type = "TV"
                AND item.modelNumber = television.modelNumber;
        """
        queryDesktop = """
                SELECT * from item, desktop 
                WHERE item.type = "DESKTOP"
                AND item.modelNumber = television.modelNumber;
        """
        queryMonitor = """
                SELECT * from item, monitorDisplay 
                WHERE item.type = "MONITOR"
                AND item.modelNumber = monitorDisplay.modelNumber;
        """
        queryLaptop = """
                SELECT * from item, laptop 
                WHERE item.type = "LAPTOP"
                AND item.modelNumber = laptop.modelNumber;
        """
        

        try:
            cursor.execute(queryTablet)
            for(name,
                modelNumber, 
                quantity, 
                weight, 
                weightFormat, 
                price, 
                priceFormat, 
                brandName,
                modelNumber,
                ramSize, 
                ramFormat, 
                processorType, 
                numCores, 
                hardDriveSize,
                hardDriveFormat,
                cameraInfo, 
                batteryInfo,
                os,
                size,
                sizeFormat,
                dx,
                dy,
                dz,
                dimensionFormat) in cursor:
                result.append(Tablet(modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat, os, Dimension(dx,dy,dz,dimensionFormat), Size(size, sizeFormat), cameraInfo, batteryInfo))

            cursor.execute(queryDesktop)
            for(name,
                modelNumber, 
                quantity, 
                weight, 
                weightFormat, 
                price, 
                priceFormat, 
                brandName,
                modelNumber,
                ramSize, 
                ramFormat, 
                processorType, 
                numCores, 
                hardDriveSize,
                hardDriveFormat,
                dx,
                dy,
                dz,
                dimensionFormat) in cursor:
                result.append(Desktop(modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat, Dimension(dx, dy, dz, dimensionFormat)))

            cursor.execute(queryTv)
            for(name,
                modelNumber, 
                quantity, 
                weight, 
                weightFormat, 
                price, 
                priceFormat, 
                brandName,
                modelNumber,
                tvType, 
                dimensionFormat,
                dx,
                dy,
                dz) in cursor:
                result.append(Television(modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName, Dimension(dx, dy, dz, dimensionFormat), tvType))
            
            cursor.execute(queryMonitor)
            for(name,
                modelNumber, 
                quantity, 
                weight, 
                weightFormat, 
                price, 
                priceFormat, 
                brandName,
                modelNumber,
                size, sizeFormat) in cursor:
                result.append(MonitorDisplay(name, quantity, modelNumber, weight, weightFormat, price, priceFormat, brandName, Size(size, sizeFormat)))

            cursor.execute(queryLaptop)
            for(name,
                modelNumber, 
                quantity, 
                weight, 
                weightFormat, 
                price, 
                priceFormat, 
                brandName,
                modelNumber,
                ramSize, 
                ramFormat, 
                processorType, 
                numCores, 
                hardDriveSize,
                hardDriveFormat,
                containCamera, 
                isTouch,
                batteryInfo,
                os,
                size,
                sizeFormat) in cursor:
                result.append(Laptop(modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat, containCamera, isTouch, batteryInfo, os, Size(size, sizeFormat)))      
        
        except Exception as error: 
            print(error)    

        connection.commit()
        connection.close()

        return result

    def generateItemQuery(self, type, name, modelNumber, quantity, weight, wf, price, pf, brandname):
        qry = """
            INSERT INTO item (type, 
                              name,
                              modelNumber, 
                              quantity, 
                              weight, 
                              weightFormat, 
                              price, 
                              priceFormat, 
                              brandName)
                VALUES(
                    '{}',
                    '{}',
                     '{}',
                     {},
                    {},
                     '{}',
                    {},
                    '{}',
                    '{}'
                );
        """.format(type, modelNumber, name, quantity, weight, wf, price, pf, brandname)
        return qry

if __name__ == '__main__':
    
    inv = Inventory()
    tab = Television("myname", 5, "model10", 4, "kg", 400, "CAD", "brand", Size(4,"cm"));
    inv.addItem(tab)
    #print(tab)