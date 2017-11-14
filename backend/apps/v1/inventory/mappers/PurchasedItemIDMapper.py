from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID
from backend.apps.v1.inventory.TDGs.PurchasedItemIDTDG import PurchasedItemIDTDG

class PurchasedItemIDMapper():

    @staticmethod
    def insert(newPurchaseItem):

        PurchasedItemIDTDG.insert(newPurchaseItem.itemID, newPurchaseItem.customer.email, newPurchaseItem.timeStamp)
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
