from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class AbstractComputer(ItemSpecification):

    """Constructor"""

    def __init__(self, modelNumber, name, quantity, weight, 
                 weightFormat, price, priceFormat, brandName,type,
                 ramSize, ramFormat, processorType, numCores, 
                 hardDriveSize, hardDriveFormat):

        super().__init__(modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName,type)
        self.ramSize = ramSize
        self.ramFormat = ramFormat
        self.processorType = processorType
        self.numCores = numCores
        self.hardDriveSize = hardDriveSize
        self.hardDriveFormat = hardDriveFormat
