from backend.utils.database import Database

from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Dimension import Dimension
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Size import Size
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.apps.v1.inventory.models.Television import Television


class Inventory(object):
    """Constructor"""
    def __init__(self):
        pass

    def addItem(self, itemSpec):

        with Database() as cursor:

            if type(itemSpec) is Laptop:

                touch = 1 if itemSpec.isTouch else 0
                cam = 1 if itemSpec.containCamera else 0

                itemQuery = self.generateItemQuery(
                    "LAPTOP", itemSpec.modelNumber, itemSpec.name,
                    itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat,
                    itemSpec.price, itemSpec.priceFormat, itemSpec.brandName
                )

                query = """
                    INSERT INTO laptop (modelNumber, ramSize, ramFormat,
                        processorType, numCores, hardDriveSize, hardDriveFormat,
                        containsCamera, isTouch, batteryInfo, os, size, sizeFormat)
                    VALUES('{}', {}, '{}',
                        '{}', {}, {}, '{}',
                        {}, {}, '{}', '{}', {}, '{}');
                """.format(
                        itemSpec.modelNumber, itemSpec.ramSize, itemSpec.ramFormat,
                        itemSpec.processorType, itemSpec.numCores, itemSpec.hardDriveSize, itemSpec.hardDriveFormat,
                        cam, touch, itemSpec.batteryInfo, itemSpec.os, itemSpec.size.size, itemSpec.size.sizeFormat
                )

            elif type(itemSpec) is Desktop:
                itemQuery = self.generateItemQuery(
                    "DESKTOP", itemSpec.modelNumber, itemSpec.quantity,
                    itemSpec.weight, itemSpec.weightFormat,
                    itemSpec.price, itemSpec.priceFormat, itemSpec.brandName
                )

                query = """
                    INSERT INTO desktop (modelNumber, ramSize, ramFormat,
                        processorType, numCores, hardDriveSize, hardDriveFormat,
                        dx ,dy, dz, dimensionFormat)
                    VALUES('{}', {}, '{}',
                        '{}', {}, {}, '{}',
                        {}, {}, {}, '{}');
                """.format(
                        itemSpec.ramSize, itemSpec.ramFormat, itemSpec.processorType, 
                        itemSpec.numCores, itemSpec.hardDriveSize, itemSpec.hardDriveFormat, itemSpec.dimension.x, 
                        itemSpec.dimension.y, itemSpec.dimension.z, itemSpec.dimension.format
                    )

            elif type(itemSpec) is MonitorDisplay:
                itemQuery = self.generateItemQuery(
                    "MONITOR", itemSpec.modelNumber, itemSpec.name, itemSpec.quantity, 
                    itemSpec.weight, itemSpec.weightFormat, 
                    itemSpec.price, itemSpec.priceFormat, itemSpec.brandName
                )

                query = """
                    INSERT INTO monitorDisplay (modelNumber,size, sizeFormat)
                    VALUES('{}', {}, '{}');
                """.format(itemSpec.modelNumber, itemSpec.size.size, itemSpec.size.sizeFormat)

            elif type(itemSpec) is Television:
                itemQuery = self.generateItemQuery(
                    "TV", itemSpec.modelNumber, itemSpec.name, itemSpec.quantity,
                    itemSpec.weight, itemSpec.weightFormat,
                    itemSpec.price, itemSpec.priceFormat, itemSpec.brandName
                )

                query = """
                    INSERT INTO television (modelNumber, tvType, dimensionFormat, dx, dy, dz)
                    VALUES('{}', '{}', '{}', {}, {}, {});
                """.format(
                    itemSpec.modelNumber, itemSpec.tvType, itemSpec.dimension.format,
                    itemSpec.dimension.x, itemSpec.dimension.y, itemSpec.dimension.z
                )

            elif type(itemSpec) is Tablet:
                itemQuery = self.generateItemQuery(
                    "TABLET", itemSpec.modelNumber, itemSpec.name, itemSpec.quantity,
                    itemSpec.weight, itemSpec.weightFormat, 
                    itemSpec.price, itemSpec.priceFormat, itemSpec.brandName
                )

                query = """
                    INSERT INTO tablet (modelNumber, ramSize, ramFormat, processorType, numCores,
                        hardDriveSize, hardDriveFormat, cameraInfo, batteryInfo, os,
                        size, sizeFormat, dx, dy, dz, dimensionFormat)
                    VALUES('{}', {}, '{}', '{}', {},
                        {}, '{}', '{}', '{}', '{}',
                        {}, '{}', {}, {}, {}, '{}'
                    );
                """.format(
                    itemSpec.modelNumber, itemSpec.ramSize, itemSpec.ramFormat,
                    itemSpec.processorType, itemSpec.numCores,
                    itemSpec.hardDriveSize, itemSpec.hardDriveFormat,
                    itemSpec.cameraInfo, itemSpec.batteryInfo, itemSpec.os,
                    itemSpec.size.size, itemSpec.size.sizeFormat,
                    itemSpec.dimension.x, itemSpec.dimension.y, itemSpec.dimension.z, itemSpec.dimension.format
                )

            print(itemQuery)
            print(query)

            try:
                cursor.execute(itemQuery)
            except Exception as error:
                print(error)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)


    def requestInventoryList(self):

        queryTablet = """
            SELECT * FROM item, tablet
            WHERE UPPER(item.type) = "TABLET"
            AND item.modelNumber = tablet.modelNumber;
        """

        queryTv = """
            SELECT * from item, television
            WHERE UPPER(item.type) = "TELEVISION"
            AND item.modelNumber = television.modelNumber;
        """
        queryDesktop = """
            SELECT * from item, desktop
            WHERE UPPER(item.type) = "DESKTOP"
            AND item.modelNumber = desktop.modelNumber;
        """

        queryMonitor = """
            SELECT * from item, monitorDisplay
            WHERE UPPER(item.type) = "MONITOR"
            AND item.modelNumber = monitorDisplay.modelNumber;
        """

        queryLaptop = """
            SELECT * from item, laptop
            WHERE UPPER(item.type) = "LAPTOP"
            AND item.modelNumber = laptop.modelNumber;
        """

        result = []

        with Database() as cursor:

            try:

                cursor.execute(queryTablet)
                for row in cursor.fetchall():                    
                    result.append(
                        Tablet(
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
                    )                 

                cursor.execute(queryDesktop)
                for row in cursor.fetchall():                    
                    result.append(
                        Desktop(
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
                    )    

                cursor.execute(queryTv)                
                for(name,
                    modelNumber,
                    quantity,
                    weight,
                    weightFormat,
                    price,
                    priceFormat,
                    brandName,
                    tvType,
                    dimensionFormat,
                    dx,
                    dy,
                    dz,
                    x,
                    y) in cursor:
                    print(3)
                    result.append(Television(modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName, Dimension(dx, dy, dz, dimensionFormat), tvType))

                cursor.execute(queryMonitor)
                for row in cursor.fetchall():                    
                    result.append(
                        MonitorDisplay(
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
                    )                

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
                    print(5)
                    result.append(Laptop(modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat, containCamera, isTouch, batteryInfo, os, Size(size, sizeFormat)))

            except Exception as error:
                print("Failed to retrieve Inventory list")
                print(error)

            print(result)

        return result

    def generateItemQuery(self, itemtype, name, modelNumber, quantity,
                          weight, wf, price, pf, brandname):
        qry = """
            INSERT INTO item (type, name, modelNumber, quantity,
                weight, weightFormat, price, priceFormat, brandName)
            VALUES(
                '{}', '{}', '{}', {},
                {}, '{}', {}, '{}', '{}'
            );
        """.format(
            itemtype, modelNumber, name, quantity,
            weight, wf, price, pf, brandname
        )
        return qry

if __name__ == '__main__':

    inv = Inventory()
    tab = Television("myname", 5, "model10", 4, "kg", 400, "CAD", "brand", Size(4,"cm"));
    inv.addItem(tab)
    #print(tab)
