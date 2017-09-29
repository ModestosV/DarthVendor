from django.conf import settings
from sqlite3 import dbapi2 as Database

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
            query1 = generateItemQuery("T",itemSpec.modelNumber, itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat, itemSPec.price, itemSpec.priceFormat, itemSpec.brandName)
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

        query = """
                SELECT * FROM item 
                LEFT JOIN tablet ON item.modelNumber = tablet.modelNumber
                LEFT JOIN desktop ON item.modelNumber = desktop.modelNumber
                LEFT JOIN monitorDisplay ON item.modelNumber = monitorDisplay.modelNumber
                LEFT JOIN laptop ON item.modelNumber = laptop.modelNumber
                LEFT JOIN television ON item.modelNumber = television.modelNumber
        """

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)    

        connection.commit()
        connection.close()

        return cursor

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
    
    inv = Inventory()
    inv.requestInventoryList()