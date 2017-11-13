from backend.utils.database import Database


class MonitorDisplayIDTDG:

    owner = None

    def findBySpec(spec):

        with Database() as cursor:

            query = """
                SELECT * FROM monitorDisplayID WHERE modelNum = '{}';
            """.format(spec.modelNumber)
            try:
                cursor.execute(query)
                resultSet = cursor.fetchall()
                return resultSet
            except Exception as error:
                print(error)
                return None

    def insert(monitorDisplayID):

        with Database() as cursor:

            query = """
                INSERT INTO monitorDisplayID (serialNum, modelNum, isLocked)
                VALUES ('{}', '{}', 0);
            """.format(monitorDisplayID.serialNumber, monitorDisplayID.spec.modelNumber)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    def update(monitorDisplayID):
        with Database() as cursor:
            isLockedInt = 1 if monitorDisplayID.isLocked else 0
            query = """
                UPDATE monitorDisplayID SET
                isLocked = {}
                WHERE serialNumber = '{}';
            """.format(isLockedInt, monitorDisplayID.serialNumber)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)


    def delete(serialNum):

        with Database() as cursor:

            query = """
                DELETE FROM monitorDisplayID WHERE serialNum = '{}';
            """.format(serialNum)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    def lock(uow):
        if MonitorDisplayIDTDG.owner is None:
            owner = uow
            return True
        else:
            return False

    def unlock(uow):
        if MonitorDisplayIDTDG.owner is uow:
            owner = None
            return True
        else:
            return False
