from backend.apps.v1.accounts.TDG.PurchaseCollectionIDTDG import PurchaseCollectionIDTDG
from backend.apps.v1.accounts.models.PurchaseCollectionID import PurchaseCollectionID
from backend.apps.v1.accounts.models.PurchaseCollection import PurchaseCollection
from backend.apps.v1.inventory.models.Purchase import Purchase
from backend.apps.v1.accounts.mapper.PurchaseCollectionIDMapper import PurchaseCollectionIDMapper

from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper
from backend.apps.v1.accounts.models.Customer import Customer

from datetime import datetime


class Cart(Customer):

    cartOwnerId = Customer.id
    cartItems = list()
    cartItemMaxSize = 7
    cartItemMinSize = 0

    @staticmethod
    def addToCart(self, itemSpec):
        if len(self.cartItems) < self.cartItemMaxSize:
            if (ItemIDMapper.lock(itemSpec.type)):
                itemIdsOfItemSpecType = ItemIDMapper.find(itemSpec)
                for itemID in itemIdsOfItemSpecType:
                    if itemID.isLocked is False:
                        #skip over item and check the next to see if unlocked
                        break
                    else:
                        #set itemID.locked to true and update database to set itemID.locked to true so no one else can obtain
                        itemID.isLocked = True
                        ItemIDMapper.update(itemID)
                        self.cartItems.append(itemID)
                        return
            else:
                #tell customer they will need to to try again later to add this item
                return
        else:
            #message user telling them they are unable to add to cart as cart is full
            return

    @staticmethod
    def removeFromCart(self, itemID):
        while len(self.cartItems) > self.cartItemsMinSize:
            if self.cartItems.length() > self.cartItemsMinSize:
                if(ItemIDMapper.lock(itemID.spec.type)):
                    itemID.isLocked = False
                    ItemIDMapper.update(itemID)
                    self.cartItems.remove(itemID)
                    ItemIDMapper.unlock(itemID.spec.type)
                    return
                else:
                    #tell customer they will need to to try again later to remove this item
                    return
            else:
                #tell customer there are no more items in cart
                return

    @staticmethod
    def checkOut(self):
        #not sure format of timestamp we want....
        timeOfCheckout = datetime.timestamp()
        while self.cartItems is not None:
            for itemID in self.cartItems:
                if itemID is not None:
                    if (ItemIDMapper.lock(itemID.spec.type) and PurchaseCollectionIDMapper.lock(PurchaseCollection, self.cartOwnerId)):
                        newPurchaseItem = Purchase(itemID, self.cartOwnerId, timeOfCheckout)
                        PurchaseCollectionIDMapper.insert(newPurchaseItem)
                        #purchaseId, serialNumber, modelNumber, userId, type, timeStamp
                        #PurchaseCollectionIDMapper.add(newPurchase)
                        ItemIDMapper.delete(itemID)
                        break
                    else:
                        # tell customer they will need to to try again later to add this item
                        return
                else:
                    # message user telling them they are unable to add to cart as cart is full
                    return
            else:
                # indicate to customer they have no items in cart
                return