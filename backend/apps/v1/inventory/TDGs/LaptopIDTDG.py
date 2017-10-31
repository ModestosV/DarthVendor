from backend.utils.database import Database


class LaptopIDTDG:

    owner = None

    def findBySpec(spec):

        with Database() as cursor:

            query = """
                SELECT * FROM laptopID WHERE modelNum = '{spec.modelNum}';
            """
            try:
                cursor.execute(query)
                resultSet = cursor.fetchall()
                return resultSet
            except Exception as error:
                print(error)
                return None


    def insert(laptopID):

        with Database() as cursor:

            query = """
                INSERT INTO laptopID (serialNum, modelNum, isLocked)
                VALUES ('{serialNum}', '{spec.modelNum}', 0);
            """.format(**laptopID)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    def delete(serialNum):

        with Database() as cursor:

            query = """
                DELETE FROM laptopID WHERE serialNum = '{serialNum}';
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    def lock(uow):
        if owner is None:
            owner = uow
            return True
        else:
            return False

    def unlock(uow):
        if owner is uow:
            owner = None
            return True
        else:
            return False
