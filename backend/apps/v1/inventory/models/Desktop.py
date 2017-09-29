from AbstractComputer import AbstractComputer


class Desktop(AbstractComputer):

    """Constructor"""
    def __init__(self, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat, dimension):
        super().__init__(ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat)
        self.dimension = dimension
