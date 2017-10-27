from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class Tablet(ItemSpecification):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName, type
                 ramSize, ramFormat, processorType, numCores,
                 hardDriveSize, hardDriveFormat, os, dimension,
                 size, cameraInfo, batteryInfo):

        """Constructor"""

        super().__init__(modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName, type
                         ramSize, ramFormat, processorType, numCores,
                         hardDriveSize, hardDriveFormat)

        self.ramSize = ramSize
        self.ramFormat = ramFormat
        self.processorType = processorType
        self.numCores = numCores
        self.hardDriveSize = hardDriveSize
        self.hardDriveFormat = hardDriveFormat
        self.os = os
        self.dimension = dimension
        self.size = size
        self.cameraInfo = cameraInfo
        self.batteryInfo = batteryInfo
