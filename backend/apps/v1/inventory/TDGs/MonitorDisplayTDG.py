from backend.utils.database import Database


class MonitorDisplayTDG:

    owner = None

    @staticmethod
    def find(modelNumber):
        
        with Database() as cursor:
            query = """
                SELECT * FROM monitorDisplay WHERE modelNumber = '{}';
            """.format(modelNumber)
            try:
                cursor.execute(query)

                result = cursor.fetchone()
                return result
            except Exception as error:
                print(error)
                return None

    @staticmethod
    def insert(monitor):

        with Database() as cursor:
            query = """
                INSERT INTO monitorDisplay (modelNumber, quantity, name, weight, weightFormat, price, priceFormat,
                                            brandName, type, size, sizeFormat)
                VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price}, '{priceFormat}',
                         '{brandName}', 'monitor', {size}, '{sizeFormat}');
            """.format(**(monitor.__dict__))

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    @staticmethod
    def update(monitor):

        with Database() as cursor:
            query = """
                UPDATE monitorDisplay SET
                quantity = {quantity},
                name = '{name}',
                weight = {weight},
                weightFormat = '{weightFormat}',
                price = {price},
                priceFormat = '{priceFormat}',
                brandName = '{brandName}',
                type = '{type}',
                size = {size},
                sizeFormat = '{sizeFormat}'
                WHERE modelNumber = '{modelNumber}';
            """.format(**(monitor.__dict__))

            try:
                cursor.execute(query)

            except Exception as error:
                print(error)

    @staticmethod
    def lock(uow):
        if MonitorDisplayTDG.owner is None:
            owner = uow
            return True
        else:
            return False

    @staticmethod
    def unlock(uow):
        if MonitorDisplayTDG.owner is uow:
            owner = None
            return True
        else:
            return False
