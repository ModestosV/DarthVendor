from AbstractComputer import AbstractComputer


class Tablet(AbstractComputer):

    """Constructor"""
    def __init__(self, os, dimension, size, cameraInfo, batteryInfo):

        super(self, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat).__init__()
        self.os = os
        self.dimension = dimension
        self.size = size
        self.cameraInfo = cameraInfo
        self.batteryInfo = batteryInfo
