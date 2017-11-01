from backend.apps.v1.inventory.models.AbstractComputer import AbstractComputer


class Desktop(AbstractComputer):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName,
                 ramSize, ramFormat, processorType, numCores,
                 hardDriveSize, hardDriveFormat, dx, dy, dz, dimensionFormat):

        """" Constructor """

        super().__init__(modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName,
                         ramSize, ramFormat, processorType, numCores,
                         hardDriveSize, hardDriveFormat)

        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.dimensionFormat = dimensionFormat
