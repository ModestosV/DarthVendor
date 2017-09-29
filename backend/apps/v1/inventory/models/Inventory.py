from django.conf import settings
from sqlite3 import dbapi2 as Database
from Television import Television
from Tablet import Tablet
from Laptop import Laptop
from MonitorDisplay import MonitorDisplay
from Desktop import Desktop


class Inventory(object):
    """Constructor"""
    def __init__(self):
        pass
	
    def addItem(self, itemSpec):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()

        
        if type(itemSpec) is Laptop:

            query1 = generateItemQuery("L",itemSpec.modelNumber, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSPec.price, itemSpec.priceFormat, itemSpec.brandName)
            query2 = """
                INSERT INTO laptop (modelNumber,
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
            """.format(itemSpec.ramSize, itemSpec.ramFormat, itemSpec.processorType, itemSpec.numCores, itemSpec.hardDriveSize, itemSpec.hardDriveFormat, itemSpec.containCamera, itemSpec.isTouch, itemSpec.batteryInfo, itemSpec.os, itemSpec.size, itemSpec.sizeFormat)

        elif type(itemSpec) is Desktop:
            query1 = generateItemQuery("D",itemSpec.modelNumber, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSPec.price, itemSpec.priceFormat, itemSpec.brandName)
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

            query1 = generateItemQuery("M",itemSpec.modelNumber, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSPec.price, itemSpec.priceFormat, itemSpec.brandName)

            query2 = """
                INSERT INTO monitorDisplay (modelNumber,size, sizeFormat)
                    VALUES(
                     {},
                    '{}',
                    '{}'
                );
            """.format(itemSpec.size, itemSpec.sizeFormat)


        elif type(itemSpec) is Television:
            query1 = generateItemQuery("TV",itemSpec.modelNumber, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSPec.price, itemSpec.priceFormat, itemSpec.brandName)
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
            query1 = generateItemQuery("T",itemSpec.modelNumber, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSPec.price, itemSpec.priceFormat, itemSpec.brandName)
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
            """.format(itemSpec.modelNumber, itemSpec.ramSize, itemSpec.ramFormat, itemSpec.processorType, itemSpec.numCores, itemSpec.hardDriveSize, itemSpec.hardDriveFormat, itemSpec.cameraInfo, itemSpec.batteryInfo, itemSpec.os, itemSpec.size, itemSpec.sizeFormat, itemSpec.dx, itemSpec.dy, itemSpec.dz, itemSpec.dimensionFormat)

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

    def generateItemQuery(self, type, modelNumber, quantity, weight, wf, price, pf, brandname):
        qry = """
            INSERT INTO item (type, 
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
                     {},
                     {},
                    '{}',
                     {},
                    '{}',
                    '{}',
                );
        """.format(type, modelNumber, quantity, weight, wf, price, pf, brandname)
        return qry

if __name__ == '__main__':
    
    #inv = Inventory()
    #tab = Tablet();
    #inv.addItem()