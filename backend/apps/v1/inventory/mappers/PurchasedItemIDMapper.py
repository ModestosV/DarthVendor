from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID
from backend.apps.v1.inventory.TDGs.PurchasedItemIDTDG import PurchasedItemIDTDG

from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper


class PurchasedItemIDMapper():

    @staticmethod
    def insert(newPurchaseItem):

        PurchasedItemIDTDG.insert(newPurchaseItem.serialNumber, newPurchaseItem.spec.modelNumber, newPurchaseItem.customer.email, newPurchaseItem.spec.type, newPurchaseItem.timeStamp)
        return

    @staticmethod
    def delete(purchaseItemID):

        PurchasedItemIDTDG.delete(purchaseItemID.purchaseId)
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
    def find(purchaseID):

        purchaseItemID = PurchasedItemIDTDG.findByPurchaseId(purchaseID)
        return purchaseItemID

    @staticmethod
    def findByUser(email):
        rows = PurchasedItemIDTDG.findByUser(email)
        result = list()
        for row in rows:
            print(row)
            itemSpec = ItemSpecMapper.find(row['modelNum'], row['type'])
            result.append(PurchasedItemID(row['serialNum'], itemSpec, email, row['type'], row['timeStamp']))
        return result
