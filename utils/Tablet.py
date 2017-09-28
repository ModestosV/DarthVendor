class Tablet(AbstractComputer):

	"""Constructor"""
    def __init__(self, modelNumber, os, dimension, size, cameraInfo, batteryInfo):
     
		super().__init__()	
        self.modelNumber = modelNumber
        self.os = os
        self.dimension = dimension
        self.size = size
        self.cameraInfo = cameraInfo
        self.batteryInfo = batteryInfo