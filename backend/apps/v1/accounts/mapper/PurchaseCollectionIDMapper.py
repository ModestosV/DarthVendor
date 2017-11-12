from backend.apps.v1.accounts.models.PurchaseCollection import PurchaseCollection
from backend.apps.v1.accounts.models.PurchaseCollectionID import PurchaseCollectionID
from backend.apps.v1.accounts.TDG.PurchaseCollectionIDTDG import PurchaseCollectionIDTDG

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
    def lock(uow):

        result = PurchaseCollectionIDTDG.lock(uow)
        return result


    @staticmethod
    def unlock(uow):

        result = PurchaseCollectionIDTDG.unlock(uow)
        return result

    @staticmethod
    def find(purchaseID):

        purchaseCollectionID = PurchaseCollectionIDTDG.findByPurchaseId(purchaseID)
        return purchaseCollectionID
