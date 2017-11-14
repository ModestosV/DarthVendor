from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID
from backend.apps.v1.inventory.TDGs.PurchasedItemIDTDG import PurchasedItemIDTDG

from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper


class PurchasedItemIDMapper():

    @staticmethod
    def insert(newPurchaseItem):

        PurchasedItemIDTDG.insert(newPurchaseItem.serialNumber, newPurchaseItem.spec.modelNumber, newPurchaseItem.email, newPurchaseItem.spec.type, newPurchaseItem.timeStamp)
        return

    @staticmethod
    def delete(serialNumber):

        PurchasedItemIDTDG.delete(serialNumber)
        return

    @staticmethod
    def update(purchaseItemID):

        PurchasedItemIDTDG.update(purchaseItemID)

    @staticmethod
    def lock(lockOwner):

        result = PurchasedItemIDTDG.lock(lockOwner)
        return result

    @staticmethod
    def unlock(lockOwner):

        result = PurchasedItemIDTDG.unlock(lockOwner)
        return result

    @staticmethod
    def find(serialNumber):

        result = PurchasedItemIDTDG.findByPurchaseId(serialNumber)
        itemSpec = ItemSpecMapper.find(result['modelNum'], result['type'])
        result = PurchasedItemID(result['serialNum'], itemSpec, result['userID'], result['type'], result['timeStamp'])
        return result

    @staticmethod
    def findByUser(email):
        rows = PurchasedItemIDTDG.findByUser(email)
        result = list()
        for row in rows:
            itemSpec = ItemSpecMapper.find(row['modelNum'], row['type'])
            result.append(PurchasedItemID(row['serialNum'], itemSpec, email, row['type'], row['timeStamp']))
        return result
