from backend.apps.v1.inventory.models.AbstractComputer import AbstractComputer


class Desktop(AbstractComputer):

    """Constructor"""
    def __init__(self, dimension):
        super().__init__(ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat)
        self.dimension = dimension
