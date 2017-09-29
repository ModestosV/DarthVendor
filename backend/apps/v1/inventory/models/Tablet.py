from AbstractComputer import AbstractComputer


class Tablet(AbstractComputer):

    """Constructor"""
    def __init__(self, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat, os, dimension, size, cameraInfo, batteryInfo):

        super().__init__(ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat)
        self.os = os
        self.dimension = dimension
        self.size = size
        self.cameraInfo = cameraInfo
        self.batteryInfo = batteryInfo
