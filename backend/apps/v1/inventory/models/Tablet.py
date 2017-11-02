from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class Tablet(ItemSpecification):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName,
                 ramSize, ramFormat, processorType, numCores,
                 hardDriveSize, hardDriveFormat, os, dx, dy, dz,
                 size, cameraInfo, batteryInfo):

        """Constructor"""

        super().__init__(modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName, "TABLET")

        self.ramSize = ramSize
        self.ramFormat = ramFormat
        self.processorType = processorType
        self.numCores = numCores
        self.hardDriveSize = hardDriveSize
        self.hardDriveFormat = hardDriveFormat
        self.os = os
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.dimensionFormat = "cm"
        self.size = size
        self.sizeFormat = "inch"
        self.cameraInfo = cameraInfo
        self.batteryInfo = batteryInfo
