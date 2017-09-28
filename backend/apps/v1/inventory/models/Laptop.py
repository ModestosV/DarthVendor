from AbstractComputer import AbstractComputer


class Laptop(AbstractComputer):

    """Constructor"""
    def __init__(self, modelNumber, containCamera, isTouch, batteryInfo, os, size, sizeFormat):

        """AbstractComputer.__init__(self, modelNumber, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat)"""

        super().__init__()
        self.containCamera = containCamera
        self.isTouch = isTouch
        self.batteryInfo = batteryInfo
        self.os = os
        self.size = size
        self.sizeFormat = sizeFormat
