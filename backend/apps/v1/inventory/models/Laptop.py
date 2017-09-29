#from backend.apps.v1.inventory.models.AbstractComputer import AbstractComputer
from AbstractComputer import AbstractComputer


class Laptop(AbstractComputer):

    """Constructor"""

    def __init__(self, modelNumber, name, 
                quantity, weight, weightFormat, 
                price, priceFormat, brandName, 
                ramSize, ramFormat, processorType, 
                numCores, hardDriveSize, hardDriveFormat, 
                containCamera, isTouch, batteryInfo, os, size):

        super().__init__(modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat)

        self.containCamera = containCamera
        self.isTouch = isTouch
        self.batteryInfo = batteryInfo
        self.os = os
        self.size = size
