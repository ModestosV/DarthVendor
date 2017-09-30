from backend.apps.v1.inventory.models.AbstractComputer import AbstractComputer


class Tablet(AbstractComputer):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName,
                 ramSize, ramFormat, processorType, numCores,
                 hardDriveSize, hardDriveFormat, os, dimension,
                 size, cameraInfo, batteryInfo):

        """Constructor"""

        super().__init__(modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName,
                         ramSize, ramFormat, processorType, numCores,
                         hardDriveSize, hardDriveFormat)

        self.os = os
        self.dimension = dimension
        self.size = size
        self.cameraInfo = cameraInfo
        self.batteryInfo = batteryInfo
