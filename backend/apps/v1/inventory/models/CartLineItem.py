from datetime import datetime


class CartLineItem:

    # itemIDs: list of itemIDs
    def __init__(self, itemID):

        """Constructor"""
        self.itemID = itemID
        self.additionTime = datetime.now()

    def getSubTotal(self):
        return self.itemID.getPrice()
