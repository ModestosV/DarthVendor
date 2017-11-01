from backend.apps.v1.inventory.models.AbstractComputer import AbstractComputer


class Tablet(AbstractComputer):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName,
                 ramSize, ramFormat, processorType, numCores,
                 hardDriveSize, hardDriveFormat, os, dx, dy, dz, dimensionFormat,
                 size, sizeFormat, cameraInfo, batteryInfo):

        """Constructor"""

        super().__init__(modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName,
                         ramSize, ramFormat, processorType, numCores,
                         hardDriveSize, hardDriveFormat)

        self.os = os
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.dimensionFormat
        self.size = size
        self.sizeFormat = sizeFormat
        self.cameraInfo = cameraInfo
        self.batteryInfo = batteryInfo
