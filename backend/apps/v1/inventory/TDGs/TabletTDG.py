from backend.apps.v1.inventory.models.Dimension import Dimension
from backend.apps.v1.inventory.models.Size import Size
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.utils.database import Database


class TabletTDG:
    owner = None

    @staticmethod
    def insert(tablet):

        with Database() as cursor:
            itemQuery = self.generateItemQuery(
                "TABLET", itemSpec.modelNumber, itemSpec.name,
                itemSpec.quantity, itemSpec.weight, itemSpec.weightFormat,
                itemSpec.price, itemSpec.priceFormat, itemSpec.brandName
            )

            query = """
                INSERT INTO tablet (modelNumber, quantity, name, weight, weightFormat, price, priceFormat, brandName,
                    type, ramSize, ramFormat, processorType, numCores,
                    hardDriveSize, hardDriveFormat, os, batteryInfo,
                    dx, dy, dz, dimensionFormat, cameraInfo, size, sizeFormat)
                VALUES('{}', {}, '{}', {}, '{}',
                    {}, '{}', '{}', '{}', '{}', '{}'
                    '{}', {}, {}, '{}',
                    '{}', '{}', '{}',
                );
            """.format(
                itemSpec.modelNumber, itemSpec.quantity, itemSpec.name, itemSpec.weight, itemSpec.weightFormat,
                itemSpec.price, itemSpec.priceFormat, itemSpec.brandName, itemSpec.type, itemSpec.ramSize, itemSpec.ramFormat,
                itemSpec.processorType, itemSpec.numCores, itemSpec.hardDriveSize, itemSpec.hardDriveFormat,
                itemSpec.os, itemSpec.batteryInfo, itemSpec.dimension.x, itemSpec.dimension.y, itemSpec.dimension.z,
                itemSpec.dimension.format, itemSpec.cameraInfo, itemSpec.size.size, itemSpec.size.sizeFormat
            )
