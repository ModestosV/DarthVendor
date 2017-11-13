from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID
from backend.apps.v1.inventory.TDGs.PurchasedItemIDTDG import PurchasedItemIDTDG

class PurchaseCollectionIDMapper():

    @staticmethod
    def insert(newPurchaseItem):

        PurchaseCollectionIDTDG.insert(newPurchaseItem.itemID, newPurchaseItem.userId, newPurchaseItem.timeOfCheckout)
        return

    @staticmethod
    def delete(purchaseCollectionID):

        PurchaseCollectionIDTDG.delete(purchaseCollectionID.purchaseId)
        return

    @staticmethod
    def update(purchaseCollectionID):

        PurchaseCollectionIDTDG.update(purchaseCollectionID)

    @staticmethod
    def lock(lockOwner):

        result = PurchaseCollectionIDTDG.lock(lockOwner)
        return result

    @staticmethod
    def unlock(lockOwner):

        result = PurchaseCollectionIDTDG.unlock(lockOwner)
        return result

    @staticmethod
    def find(purchaseID):

        purchaseCollectionID = PurchaseCollectionIDTDG.findByPurchaseId(purchaseID)
        return purchaseCollectionID
