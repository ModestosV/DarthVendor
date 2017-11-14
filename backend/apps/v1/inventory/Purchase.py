from backend.apps.v1.inventory.models.Cart import Cart
from backend.apps.v1.inventory.mappers.PurchaseCollectionIDMapper import PurchaseCollectionIDMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper


class Purchase():

    def __init__(self, customer):
        self.customer = customer
        self.cart = None

    def addItem(self, itemSpec):
        if self.cart is None:
            self.cart = Cart(self.customer)

        self.cart.addToCart(itemSpec)

    def removeItem(self, itemID):
        self.cart.removeItem(itemID)

    def confirmPurchase(self):
        self.cart.confirmPurchase()

    def getCart(self):
        return self.cart

    def returnItems(self,idList):
        for purchaseID in idList:
            result = PurchaseCollectionIDMapper.delete(purchaseID)
            if result == False:
                return result

        for purchaseID in idList:
            result = ItemIDMapper.insert(purchaseID.itemID)
            if result == False:
                return result

        return result

    def initiateReturn():
        resultSet = PurchaseCollectionIDMapper.find("")
        return resultSet
