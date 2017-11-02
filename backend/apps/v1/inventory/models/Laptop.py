from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class Laptop(ItemSpecification):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName, type,
                 ramSize, ramFormat, processorType, numCores,
                 hardDriveSize, hardDriveFormat,
                 containCamera, isTouch, batteryInfo, os, size):

        """" Constructor """

        super().__init__(modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName, "Laptop")

        
        self.ramSize = ramSize
        self.ramFormat = ramFormat
        self.processorType = processorType
        self.numCores = numCores
        self.hardDriveSize = hardDriveSize
        self.hardDriveFormat = hardDriveFormat
        self.containCamera = containCamera
        self.isTouch = isTouch
        self.batteryInfo = batteryInfo
        self.os = os
        self.size = size
        self.sizeFormat = "inch"