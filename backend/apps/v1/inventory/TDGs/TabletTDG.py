from backend.apps.v1.inventory.models.Dimension import Dimension
from backend.apps.v1.inventory.models.Size import Size
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.utils.database import Database


class TabletTDG:
    owner = None

    @staticmethod
    def insert(tablet):

        with Database() as cursor:
            query = """
                INSERT INTO tablet (modelNumber, quantity, name, weight, weightFormat, price, priceFormat, brandName,
                                    type, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat,
                                    os, batteryInfo, dx, dy, dz, dimensionFormat, cameraInfo, size, sizeFormat)
                VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price}, '{priceFormat}',
                                    '{brandName}', '{type}', {ramSize}, '{ramFormat}', '{processorType}', {numCores},
                                    {hardDriveSize}, '{hardDriveFormat}', '{os}', '{batteryInfo}', {dx}, {dy}, {dz},
                                    '{dimensionFormat}', '{cameraInfo}', {size}, '{sizeFormat}');
            """.format(**tablet)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
