from backend.utils.database import Database
from backend.apps.v1.inventory.models.Desktop import Desktop


class DesktopTDG:

    owner = None

    @staticmethod
    def findAll():
        with Database() as cursor:
            query = """
                    SELECT * FROM desktop WHERE modelNumber NOT IN (SELECT modelNumber FROM deleteFlag);
                """

            try:
                cursor.execute(query)

                result = cursor.fetchall()
                return result
            except Exception as error:
                print(error)
                return None

    @staticmethod
    def find(modelNumber):

        with Database() as cursor:
            query = """
                    SELECT * FROM desktop WHERE modelNumber = '{}';
                """.format(modelNumber)

            try:
                cursor.execute(query)

                result = cursor.fetchone()
                return result
            except Exception as error:
                print(error)
                return None

    @staticmethod
    def insert(desktop):
        with Database() as cursor:

            query = """
                INSERT INTO desktop (modelNumber, quantity, name, weight, weightFormat, price,
                    priceFormat, brandName, type, ramSize, ramFormat, processorType, numCores, hardDriveSize,
                    hardDriveFormat, dx, dy, dz, dimensionFormat)
                VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price},
                    '{priceFormat}', '{brandName}', 'desktop', {ramSize}, '{ramFormat}', '{processorType}', {numCores}, {hardDriveSize},
                    '{hardDriveFormat}', {dx}, {dy}, {dz}, '{dimensionFormat}');
            """.format(**(desktop.__dict__))

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    @staticmethod
    def update(desktop):

        with Database() as cursor:
            query = """
                    UPDATE desktop SET
                    quantity = {quantity},
                    name = '{name}',
                    weight = {weight},
                    weightFormat = '{weightFormat}',
                    price = {price},
                    priceFormat = '{priceFormat}',
                    brandName = '{brandName}',
                    ramSize = {ramSize},
                    ramFormat = '{ramFormat}',
                    processorType = '{processorType}',
                    numCores = '{numCores}',
                    hardDriveSize = '{hardDriveSize}',
                    hardDriveFormat = '{hardDriveFormat}',
                    dx = '{dx}',
                    dy = '{dy}',
                    dz = '{dz}',
                    dimensionFormat = '{dimensionFormat}',
                    type = '{type}'
                    WHERE modelNumber = '{modelNumber}';
                """.format(**(desktop.__dict__))

            try:
                cursor.execute(query)

            except Exception as error:
                print(error)
                
    @staticmethod
    def delete(desktop):

        with Database() as cursor:
            query = """
                INSERT INTO deleteFlag (modelNumber, type)
                VALUES ('{modelNumber}', 'desktop');
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    @staticmethod
    def lock(uow):
        if DesktopTDG.owner is None:
            owner = uow
            return True
        else:
            return False

    @staticmethod
    def unlock(uow):
        if DesktopTDG.owner is uow:
            owner = None
            return True
        else:
            return False
