from backend.apps.v1.inventory.models.Cart import Cart
from backend.apps.v1.inventory.mappers.PurchasedItemIDMapper import PurchasedItemIDMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper
from backend.apps.v1.inventory.models.ItemID import ItemID


class Purchase():

    def __init__(self, customer):
        self.customer = customer
        self.cart = None

    def addItem(self, itemSpec):
        if self.cart is None:
            self.cart = Cart(self.customer)

        self.cart.addItem(itemSpec)

    def removeItem(self, itemID):
        self.cart.removeItem(itemID)

    def confirmPurchase(self):
        self.cart.confirmPurchase()
        self.cart.stopCartClean()
        self.cart = None

    def getCart(self):
        return self.cart

    def returnItems(self, idList):

        for purchaseID in idList:
            PurchasedItemIDMapper.delete(purchaseID.serialNumber)
            itemID = ItemID(purchaseID.serialNumber, False, purchaseID.spec)
            ItemIDMapper.insert(itemID)

        return

    def getPurchaseCollection(self, user):

        return PurchasedItemIDMapper.findByUser(user.email)
