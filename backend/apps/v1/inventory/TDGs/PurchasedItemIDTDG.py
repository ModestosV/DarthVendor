from backend.apps.v1.inventory.models.PurchaseCollection import PurchaseCollection
from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID

from backend.utils.database import Database


class PurchasedItemIDTDG:

    owner = None

    def findByPurchaseId(purchaseID):

        with Database() as cursor:

                query = """
                    SELECT * FROM purchasecollection WHERE purchaseId = '{}';
                """.format(purchaseID)
                try:
                    cursor.execute(query)
                    resultSet = cursor.fetchall()
                    return resultSet
                except Exception as error:
                    print(error)
                    return None

    def findByUserId(userId):

        with Database() as cursor:

                query = """
                  SELECT * FROM purchasecollection WHERE userId = '{}';
                """.format(userId)
                try:
                    cursor.execute(query)
                    result = cursor.fetchone()
                    return result
                except Exception as error:
                    print(error)
                    return None

    def insert(itemID, userId, timeOfCheckout):

        with Database() as cursor:

                query = """
                    INSERT INTO purchasecollection (serialNum, modelNum, userId, type, timeStamp)
                    VALUES ('{}', '{}','{}','{}','{}');
                """.format(itemID.serialNumber, itemID.spec.modelNumber, userId, itemID.spec.type, timeOfCheckout)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

    def update(purchaseCollectionID):

        # needs to have update method implimented for database entry where serialNumber matches and match up other criteria of object
        return

    def delete(purchaseCollectionID):

        with Database() as cursor:

                query = """
                DELETE FROM purchasecollection WHERE purchaseCollectionID.purchaseId = '{}';
                """.format(purchaseCollectionID.purchaseId)

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
