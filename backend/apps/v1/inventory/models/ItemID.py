class ItemID(object):

    def __init__(self, serialNumber, isLocked, itemSpecification):

        """Constructor"""

        self.serialNumber = serialNumber
        self.isLocked = isLocked
        self.spec = itemSpecification

    def getPrice(self):
        return self.spec.price
