from backend.utils.database import Database
from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Dimension import Dimension
from backend.apps.v1.inventory.models.Size import Size


class DesktopTDG:

    owner = None

    @staticmethod
    def insert(desktop):
        with Database() as cursor:

            query = """
                INSERT INTO desktop (modelNumber, quantity, name, weight, weightFormat, price, priceFormat, brandName, type, ramSize, ramFormat,
                    processorType, numCores, hardDriveSize, hardDriveFormat,
                    dx ,dy, dz, dimensionFormat)
                VALUES('{}', {}, '{}', {}, '{}',
                    {}, '{}', '{}', '{}', {}, '{}'
                    '{}', {}, {}, '{}',
                    {}, {}, {}, '{}');
            """.format(
                    desktop.modelNumber, desktop.quantity, desktop.name, desktop.weight, desktop.weightFormat,
                    desktop.price, desktop.priceFormat, desktop.brandName, desktop.type, desktop.ramSize, desktop.ramFormat,
                    desktop.processorType, desktop.numCores, desktop.hardDriveSize, desktop.hardDriveFormat,
                    desktop.dimension.x, desktop.dimension.y, desktop.dimension.z, desktop.dimension.format
            )
            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
