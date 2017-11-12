from backend.utils.database import Database


class TabletIDTDG:

    owner = None

    def findBySpec(spec):

        with Database() as cursor:

            query = """
                SELECT * FROM tabletID WHERE modelNum = '{}';
            """.format(spec.modelNumber)
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
            """.format(tabletID.serialNumber, tabletID.spec.serialNumber)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    def update(tabletID):

        # needs to have update method implimented for database entry where serialNumber matches and match up other criteria of object
        return

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
        if TabletIDTDG.owner is None:
            owner = uow
            return True
        else:
            return False

    def unlock(uow):
        if TabletIDTDG.owner is uow:
            owner = None
            return True
        else:
            return False
