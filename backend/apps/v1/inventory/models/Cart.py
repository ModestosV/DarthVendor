from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID
from backend.apps.v1.inventory.models.PurchaseCollection import PurchaseCollection
from backend.apps.v1.inventory.models.CartLineItem import CartLineItem
from backend.apps.v1.inventory.mappers.PurchasedItemIDMapper import PurchasedItemIDMapper

from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper

from datetime import datetime


class Cart():

    def __init__(self, customer):
        self.customer = customer
        self.cartItems = list()
        self.cartItemMaxSize = 7
        self.cartItemMinSize = 0
        self.Total = 0

    def addItem(self, itemSpec):
        if len(self.cartItems) < self.cartItemMaxSize:
            if (ItemIDMapper.lock(itemSpec.type, self)):
                itemIdsOfItemSpecType = ItemIDMapper.find(itemSpec)
                itemIDFound = False
                for itemID in itemIdsOfItemSpecType:
                    print(itemID.isLocked)
                    if itemID.isLocked is False:
                        # set itemID.locked to true and update database to set itemID.locked to true so no one else can obtain
                        itemID.isLocked = True
                        ItemIDMapper.update(itemID)
                        cartLineItem = CartLineItem(itemID)
                        self.cartItems.append(cartLineItem)
                        self.Total += cartLineItem.getSubTotal()
                        itemIDFound = True
                        print(self.cartItems)
                        break

                if itemIDFound is not True:
                    return False  # No stock of this item
                ItemIDMapper.unlock(itemSpec.type, self)

            else:
                # tell customer they will need to to try again later to add this item
                return False
        else:
            # message user telling them they are unable to add to cart as cart is full
            return False

        return True

    def removeItem(self, itemID):
        if len(self.cartItems) > self.cartItemMinSize:

            if(ItemIDMapper.lock(itemID.spec.type, self)):
                itemID.isLocked = False
                ItemIDMapper.update(itemID)
                for cartLineItem in self.cartItems:
                    if cartLineItem.itemID.serialNumber == itemID.serialNumber:
                        self.cartItems.remove(cartLineItem)
                ItemIDMapper.unlock(itemID.spec.type, self)
                return
            else:
                # tell customer they will need to to try again later to remove this item
                return
        else:
            # tell customer there are no more items in cart
            return

    def confirmPurchase(self):
        timeOfCheckout = datetime.now()
        for cartLineItem in self.cartItems:
            if cartLineItem is not None:
                if (ItemIDMapper.lock(cartLineItem.itemID.spec.type, self) and PurchasedItemIDMapper.lock(self)):
                    newPurchaseItem = PurchasedItemID(None, cartLineItem.itemID, self.customer, cartLineItem.itemID.spec.type, timeOfCheckout)
                    PurchasedItemIDMapper.insert(newPurchaseItem)
                    ItemIDMapper.delete(cartLineItem.itemID.serialNumber, cartLineItem.itemID.spec.type)

                    ItemIDMapper.unlock(cartLineItem.itemID.spec.type, self)
                    PurchasedItemIDMapper.unlock(self)
                    break
                else:
                    # tell customer they will need to to try again later to add this item
                    return False

        return True
