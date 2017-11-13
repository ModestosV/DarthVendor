from backend.utils.database import Database


class LaptopTDG:

    owner = None

    @staticmethod
    def findAll():

        with Database() as cursor:
            query = """
                    SELECT * FROM laptop;
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
                    SELECT * FROM laptop WHERE modelNumber = '{}';
                """.format(modelNumber)

            try:
                cursor.execute(query)

                result = cursor.fetchone()
                return result
            except Exception as error:
                print(error)
                return None

    @staticmethod
    def insert(laptop):

        with Database() as cursor:
            query = """
                INSERT INTO laptop (modelNumber, quantity, name, weight, weightFormat, price, priceFormat, brandName,
                                    type, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat,
                                    os, batteryInfo, dx, dy, dz, dimensionFormat, cameraInfo, size, sizeFormat)
                VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price}, '{priceFormat}',
                                    '{brandName}', 'laptop', {ramSize}, '{ramFormat}', '{processorType}', {numCores},
                                    {hardDriveSize}, '{hardDriveFormat}', '{os}', '{batteryInfo}', {dx}, {dy}, {dz},
                                    '{dimensionFormat}', '{cameraInfo}', {size}, '{sizeFormat}');
            """.format(**laptop)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    @staticmethod
    def update(laptop):

        with Database() as cursor:
            query = """
                UPDATE laptop SET
                quantity = {quantity},
                    name = '{name}',
                    weight = {weight},
                    weightFormat = '{weightFormat}',
                    price = {price},
                    priceFormat = '{priceFormat}',
                    brandName = '{brandName}',
                    type = 'laptop',
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
                    size = {size},
                    sizeFormat = '{sizeFormat}'
                    WHERE modelNumber = '{modelNumber}';
            """.format(**(laptop.__dict__))

            try:
                cursor.execute(query)

            except Exception as error:
                print(error)

    @staticmethod
    def lock(uow):
        if LaptopTDG.owner is None:
            owner = uow
            return True
        else:
            return False

    @staticmethod
    def unlock(uow):
        if LaptopTDG.owner is uow:
            owner = None
            return True
        else:
            return False
