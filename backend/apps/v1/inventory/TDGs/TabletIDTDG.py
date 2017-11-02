from backend.utils.database import Database


class TabletIDTDG:

    owner = None

    def findBySpec(spec):

        with Database() as cursor:

            query = """
                SELECT * FROM tabletID WHERE modelNum = '{}';
            """.format(spec.modelNum)
            try:
                cursor.execute(query)
                resultSet = cursor.fetchall()
                return resultSet
            except Exception as error:
                print(error)
                return None

    def insert(tabletID):

        with Database() as cursor:

            query = """
                INSERT INTO tabletID (serialNum, modelNum, isLocked)
                VALUES ('{}', '{}', 0);
            """.format(tabletID.serialNum, tabletID.spec.serialNum)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    def delete(serialNum):

        with Database() as cursor:

            query = """
                DELETE FROM tabletID WHERE serialNum = '{}';
            """.format(serialNum)

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
