from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.utils.database import Database


class Inventory(object):

    def __init__(self):
        """ Constructor. """
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
                    "DESKTOP", itemSpec.modelNumber, itemSpec.name,
                    itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat,
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
                        itemSpec.modelNumber, itemSpec.ramSize, itemSpec.ramFormat,
                        itemSpec.processorType, itemSpec.numCores, itemSpec.hardDriveSize, itemSpec.hardDriveFormat,
                        itemSpec.dimension.x, itemSpec.dimension.y, itemSpec.dimension.z, itemSpec.dimension.format)

            elif type(itemSpec) is MonitorDisplay:
                itemQuery = self.generateItemQuery(
                    "MONITOR", itemSpec.modelNumber, itemSpec.name,
                    itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat,
                    itemSpec.price, itemSpec.priceFormat, itemSpec.brandName
                )

                query = """
                    INSERT INTO monitorDisplay (modelNumber,size, sizeFormat)
                    VALUES('{}', {}, '{}');
                """.format(itemSpec.modelNumber, itemSpec.size.size, itemSpec.size.sizeFormat)

            elif type(itemSpec) is Tablet:
                itemQuery = self.generateItemQuery(
                    "TABLET", itemSpec.modelNumber, itemSpec.name,
                    itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat,
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

            try:
                cursor.execute(itemQuery)
                print("Item Added")
            except Exception as error:
                print(error)

            try:
                cursor.execute(query)
                print("{} Added".format(itemSpec.__class__.__name__))
            except Exception as error:
                print(error)


    def requestInventoryList(self):

        # queryTablet = """
        #     SELECT * FROM item, tablet
        #     WHERE UPPER(item.type) = "TABLET"
        #     AND item.modelNumber = tablet.modelNumber;
        # """
        #
        # queryDesktop = """
        #     SELECT * from item, desktop
        #     WHERE UPPER(item.type) = "DESKTOP"
        #     AND item.modelNumber = desktop.modelNumber;
        # """
        #
        # queryMonitor = """
        #     SELECT * from item, monitorDisplay
        #     WHERE UPPER(item.type) = "MONITOR"
        #     AND item.modelNumber = monitorDisplay.modelNumber;
        # """
        #
        # queryLaptop = """
        #     SELECT * from item, laptop
        #     WHERE UPPER(item.type) = "LAPTOP"
        #     AND item.modelNumber = laptop.modelNumber;
        # """
        #
        # result = list()
        #
        # with Database() as cursor:
        #
        #     try:
        #
        #         cursor.execute(queryTablet)
        #         for row in cursor.fetchall():
        #             result.append(
        #                 Tablet(
        #                     row.get('modelNumber'),
        #                     row.get('name'),
        #                     row.get('quantity'),
        #                     row.get('weight'),
        #                     row.get('weightFormat'),
        #                     row.get('price'),
        #                     row.get('priceFormat'),
        #                     row.get('brandName'),
        #                     row.get('ramSize'),
        #                     row.get('ramFormat'),
        #                     row.get('processorType'),
        #                     row.get('numCores'),
        #                     row.get('hardDriveSize'),
        #                     row.get('hardDriveFormat'),
        #                     row.get('os'),
        #                     Dimension(
        #                         row.get('dx'),
        #                         row.get('dy'),
        #                         row.get('dz'),
        #                         row.get('dimensionFormat'),
        #                     ),
        #                     Size(
        #                         row.get('size'),
        #                         row.get('sizeFormat')
        #                     ),
        #                     row.get('cameraInfo'),
        #                     row.get('batteryInfo')
        #                 )
        #             )
        #
        #         cursor.execute(queryDesktop)
        #         for row in cursor.fetchall():
        #             result.append(
        #                 Desktop(
        #                     row.get('modelNumber'),
        #                     row.get('name'),
        #                     row.get('quantity'),
        #                     row.get('weight'),
        #                     row.get('weightFormat'),
        #                     row.get('price'),
        #                     row.get('priceFormat'),
        #                     row.get('brandName'),
        #                     row.get('ramSize'),
        #                     row.get('ramFormat'),
        #                     row.get('processorType'),
        #                     row.get('numCores'),
        #                     row.get('hardDriveSize'),
        #                     row.get('hardDriveFormat'),
        #                     Dimension(
        #                         row.get('dx'),
        #                         row.get('dy'),
        #                         row.get('dz'),
        #                         row.get('dimensionFormat'),
        #                     ),
        #                 )
        #             )
        #
        #         cursor.execute(queryMonitor)
        #         for row in cursor.fetchall():
        #             result.append(
        #                 MonitorDisplay(
        #                     row.get('modelNumber'),
        #                     row.get('name'),
        #                     row.get('quantity'),
        #                     row.get('weight'),
        #                     row.get('weightFormat'),
        #                     row.get('price'),
        #                     row.get('priceFormat'),
        #                     row.get('brandName'),
        #                     Size(
        #                         row.get('size'),
        #                         row.get('sizeFormat')
        #                     )
        #                 )
        #             )
        #
        #         cursor.execute(queryLaptop)
        #         for row in cursor.fetchall():
        #             result.append(
        #                 Laptop(
        #                     row.get('modelNumber'),
        #                     row.get('name'),
        #                     row.get('quantity'),
        #                     row.get('weight'),
        #                     row.get('weightFormat'),
        #                     row.get('price'),
        #                     row.get('priceFormat'),
        #                     row.get('brandName'),
        #                     row.get('ramSize'),
        #                     row.get('ramFormat'),
        #                     row.get('processorType'),
        #                     row.get('numCores'),
        #                     row.get('hardDriveSize'),
        #                     row.get('hardDriveFormat'),
        #                     row.get('containsCamera'),
        #                     row.get('isTouch'),
        #                     row.get('batteryInfo'),
        #                     row.get('os'),
        #                     Size(
        #                         row.get('size'),
        #                         row.get('sizeFormat')
        #                     )
        #                 )
        #             )
        #
        #
        #     except Exception as error:
        #         print("Failed to retrieve Inventory list")
        #         print(error)
        #
        #     print("{} UNIQUE items found".format(len(result)))

        return result

    def generateItemQuery(self, itemtype, modelNumber, name, quantity,
                          weight, wf, price, pf, brandName):
        qry = """
            INSERT INTO item (type, modelNumber, name, quantity,
                weight, weightFormat, price, priceFormat, brandName)
            VALUES(
                '{}', '{}', '{}', {},
                {}, '{}', {}, '{}', '{}'
            );
        """.format(
            itemtype, modelNumber, name, quantity,
            weight, wf, price, pf, brandName
        )
        return qry
