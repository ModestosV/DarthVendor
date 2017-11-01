from backend.apps.v1.inventory.models.Dimension import Dimension
from backend.apps.v1.inventory.models.Size import Size
from backend.apps.v1.inventory.models.Tablet import Tablet
from backend.utils.database import Database


class TabletTDG:
    owner = None

    @staticmethod
    def find(modelNumber):

        with Database() as cursor:
            query = """
                    SELECT * FROM tablet WHERE modelNumber = '{}';
                """.format(modelNumber)

            try:
                cursor.execute(query)

                result = cursor.fetchone()
                return result
            except Exception as error:
                print(error)
                return None

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
            """.format(**(tablet.__dict__))

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    @staticmethod
    def update(tablet):

        with Database() as cursor:
            query = """
                    UPDATE tablet SET
                    quantity = {quantity},
                    name = '{name}',
                    weight = {weight},
                    weightFormat = '{weightFormat}',
                    price = {price},
                    priceFormat = '{priceFormat}',
                    brandName = '{brandName}',
                    ramSize = '{ramSize}',
                    ramFormat = {ramFormat},
                    processorType = '{processorType}',
                    numCores = '{numCores}',
                    hardDriveSize = '{hardDriveSize}',
                    hardDriveFormat = '{hardDriveFormat}',
                    os ='{os}',
                    batteryInfo ='{batteryInfo}',
                    dx = '{dx}',
                    dy = '{dy}',
                    dz = '{dz}',
                    dimensionFormat = '{dimensionFormat}',
                    cameraInfo = '{cameraInfo}',
                    type = '{type}',
                    size = {size},
                    sizeFormat = '{sizeFormat}'
                    WHERE modelNumber = '{modelNumber}';
                """.format(**(tablet.__dict__))

            try:
                cursor.execute(query)

            except Exception as error:
                print(error)

    @staticmethod
    def lock(uow):
        if TabletTDG.owner is None:
            owner = uow
            return True
        else:
            return False

    @staticmethod
    def unlock(uow):
        if TabletTDG.owner is uow:
            owner = None
            return True
        else:
            return False
