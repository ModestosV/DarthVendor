class ItemID(object):

    def __init__(self, serialNumber, modelNumber, isLocked, itemSpecification):

        """Constructor"""

        self.serialNumber = serialNumber
        self.modelNumber = modelNumber
        self.isLocked = isLocked
        self.spec = itemSpecification