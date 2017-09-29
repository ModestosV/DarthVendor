from backend.apps.v1.inventory.models.AbstractComputer import AbstractComputer


class Laptop(AbstractComputer):

    """Constructor"""
    def __init__(self, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat, containCamera, isTouch, batteryInfo, os, size, sizeFormat):

        super().__init__(modelNumber, weight, weightFormat, price, priceFormat, brandNameramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat)
        self.containCamera = containCamera
        self.isTouch = isTouch
        self.batteryInfo = batteryInfo
        self.os = os
        self.size = size
        self.sizeFormat = sizeFormat
