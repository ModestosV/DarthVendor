from backend.apps.v1.inventory.models.PurchasedItemID import PurchasedItemID
from backend.apps.v1.inventory.models.PurchaseCollection import PurchaseCollection
from backend.apps.v1.inventory.models.CartLineItem import CartLineItem
from backend.apps.v1.inventory.mappers.PurchasedItemIDMapper import PurchasedItemIDMapper

from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper

from backend.apps.v1.inventory.Exceptions import TableLockedException, CartFullException, OutOfStockException

import threading
from datetime import datetime, timedelta


class Cart():
    deltaTime = timedelta(minutes=0, seconds=300)

    def __init__(self, customer):
        self.customer = customer
        self.cartItems = list()
        self.cartItemMaxSize = 7
        self.cartItemMinSize = 0
        self.Total = 0
        self.cleanCart()

    def stopCartClean(self):
        self.t.cancel()

    def cleanCart(self):
        print('clean')
        self.t = threading.Timer(5.0, self.cleanCart)
        self.t.start()
        now = datetime.now()

        for lineItem in self.cartItems:
            if now - lineItem.additionTime > Cart.deltaTime:
                self.removeItem(lineItem.itemID)

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

                ItemIDMapper.unlock(itemSpec.type, self)
                if itemIDFound is not True:
                    raise OutOfStockException()

            else:
                raise TableLockedException()
        else:
            raise CartFullException()

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
                raise TableLockedException()
        else:
            # tell customer there are no more items in cart
            return

    def confirmPurchase(self):
        timeOfCheckout = datetime.now()
        for cartLineItem in self.cartItems:
            print(cartLineItem)
            if cartLineItem is not None:
                if (ItemIDMapper.lock(cartLineItem.itemID.spec.type, self) and PurchasedItemIDMapper.lock(self)):
                    print('adding')
                    newPurchaseItem = PurchasedItemID(cartLineItem.itemID.serialNumber, cartLineItem.itemID.spec, self.customer.email, cartLineItem.itemID.spec.type, timeOfCheckout)
                    PurchasedItemIDMapper.insert(newPurchaseItem)
                    ItemIDMapper.delete(cartLineItem.itemID.serialNumber, cartLineItem.itemID.spec.type)

                    ItemIDMapper.unlock(cartLineItem.itemID.spec.type, self)
                    PurchasedItemIDMapper.unlock(self)
                else:
                    print('unlocking')
                    ItemIDMapper.unlock(cartLineItem.itemID.spec.type, self)
                    PurchasedItemIDMapper.unlock(self)
                    raise TableLockedException()

        return True
