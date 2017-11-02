from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class Tablet(ItemSpecification):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName, type,
                 ramSize, ramFormat, processorType, numCores,
                 hardDriveSize, hardDriveFormat, os, x, y, z, format,
                 size, sizeFormat, cameraInfo, batteryInfo):

        """Constructor"""

        super().__init__(modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName, "Tablet")

        self.ramSize = ramSize
        self.ramFormat = ramFormat
        self.processorType = processorType
        self.numCores = numCores
        self.hardDriveSize = hardDriveSize
        self.hardDriveFormat = hardDriveFormat
        self.os = os
        self.x = x
        self.y = y
        self.z = z
        self.format = "cm"
        self.size = size
        self.sizeFormat = "inch"
        self.cameraInfo = cameraInfo
        self.batteryInfo = batteryInfo
