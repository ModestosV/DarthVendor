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
                INSERT INTO desktop (modelNumber, quantity, name, weight, weightFormat, price,
                    priceFormat, brandName, type, ramSize, ramFormat, processorType, numCores, hardDriveSize,
                    hardDriveFormat, dx, dy, dz, dimensionFormat)
                VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price},
                    '{priceFormat}', '{brandName}', '{type}', {ramSize}, '{ramFormat}', '{processorType}', {numCores}, {hardDriveSize},
                    '{hardDriveFormat}', {dx}, {dy}, {dz}, '{dimensionFormat}');
            """.format(**desktop)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
