from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class Desktop(ItemSpecification):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName, type,
                 ramSize, ramFormat, processorType, numCores,
                 hardDriveSize, hardDriveFormat, x, y, z, format):

        """" Constructor """

        super().__init__(modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName, "Desktop")
        
        self.ramSize = ramSize
        self.ramFormat = ramFormat
        self.processorType = processorType
        self.numCores = numCores
        self.hardDriveSize = hardDriveSize
        self.hardDriveFormat = hardDriveFormat
        self.x = x
        self.y = y
        self.z = z
        self.format = "cm"
        
