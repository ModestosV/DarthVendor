from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class Tablet(ItemSpecification):

    # params should contain the following keys: modelNumber, name, quantity,
    # weight, weightFormat, price, priceFormat, brandName,
    # ramSize, ramFormat, processorType, numCores,
    # hardDriveSize, hardDriveFormat, os, dx, dy, dz,
    # size, cameraInfo, batteryInfo
    def __init__(self, params):

        """Constructor"""

        super().__init__(params['modelNumber'], params['name'], params['quantity'],
                         params['weight'], params['weightFormat'], params['price'], params['priceFormat'], params['brandName'], "TABLET")

        self.ramSize = params['ramSize']
        self.ramFormat = params['ramFormat']
        self.processorType = params['processorType']
        self.numCores = params['numCores']
        self.hardDriveSize = params['hardDriveSize']
        self.hardDriveFormat = params['hardDriveFormat']
        self.os = params['os']
        self.dx = params['dx']
        self.dy = params['dy']
        self.dz = params['dz']
        self.dimensionFormat = "cm"
        self.size = params['size']
        self.sizeFormat = "inch"
        self.cameraInfo = params['cameraInfo']
        self.batteryInfo = params['batteryInfo']
