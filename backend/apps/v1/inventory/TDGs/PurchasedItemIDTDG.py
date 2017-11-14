from backend.apps.v1.inventory.models.PurchaseCollection import PurchaseCollection
from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID

from backend.utils.database import Database


class PurchasedItemIDTDG:

    owner = None

    def findByPurchaseId(purchaseID):

        with Database() as cursor:

                query = """
                    SELECT * FROM purchasecollection WHERE serialNum = '{}';
                """.format(purchaseID)
                try:
                    cursor.execute(query)
                    resultSet = cursor.fetchone()
                    return resultSet
                except Exception as error:
                    print(error)
                    return None

    def findByUser(userId):

        with Database() as cursor:

                query = """
                  SELECT * FROM purchasecollection WHERE userId = '{}';
                """.format(userId)
                try:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                except Exception as error:
                    print(error)
                    return None

    def insert(serialNum, modelNumber, email, type, timeOfCheckout):

        with Database() as cursor:

                query = """
                    INSERT INTO purchasecollection (serialNum, modelNum, userId, type, timeStamp)
                    VALUES ('{}', '{}','{}','{}','{}');
                """.format(serialNum, modelNumber, email, type, timeOfCheckout)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

    def update(purchaseCollectionID):

        # needs to have update method implimented for database entry where serialNumber matches and match up other criteria of object
        return

    def delete(serialNumber):

        with Database() as cursor:

                query = """
                DELETE FROM purchasecollection WHERE serialNum = '{}';
                """.format(serialNumber)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

    def lock(uow):
        if PurchasedItemIDTDG.owner is None:
            owner = uow
            return True
        else:
            return False

    def unlock(uow):
        if PurchasedItemIDTDG.owner is uow:
            owner = None
            return True
        else:
            return False
