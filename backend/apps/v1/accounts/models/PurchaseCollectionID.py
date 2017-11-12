

class PurchaseCollectionID(object):

    def __init__(self, purchaseId, serialNumber, modelNumber, userId, type, timeStamp):

        """Constructor"""
        self.purchaseId = purchaseId
        self.serialNumber = serialNumber
        self.modelNumber = modelNumber
        self.userId = userId
        self.type = type
        self.timeStamp = timeStamp