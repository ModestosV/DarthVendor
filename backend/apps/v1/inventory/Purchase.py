from backend.apps.v1.inventory.models.Cart import Cart


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
        self.cart = None

    def getCart(self):
        return self.cart
