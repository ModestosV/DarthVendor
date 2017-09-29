#from backend.apps.v1.inventory.models.AbstractComputer import AbstractComputer
from AbstractComputer import AbstractComputer


class Desktop(AbstractComputer):

    """Constructor"""

    def __init__(self, modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat, dimension):
        super().__init__(modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat)

        self.dimension = dimension
