from ItemSpecification import ItemSpecification


class AbstractComputer(ItemSpecification):

    """Constructor"""
    def __init__(self, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat):

        super(self, modelNumber, weight, weightFormat, price, priceFormat, brandName).__init__()
        self.ramSize = ramSize
        self.ramFormat = ramFormat
        self.processorType = processorType
        self.numCores = numCores
        self.hardDriveSize = hardDriveSize
        self.hardDriveFormat = hardDriveFormat
