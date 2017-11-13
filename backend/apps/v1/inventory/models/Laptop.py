from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class Laptop(ItemSpecification):

    # params should contain all these keys: modelNumber, name, quantity,
    # weight, weightFormat, price, priceFormat, brandName,
    # ramSize, ramFormat, processorType, numCores,
    # hardDriveSize, hardDriveFormat,
    # containsCamera, isTouch, batteryInfo, os, size
    def __init__(self, params):

        """" Constructor """

        super().__init__(params['modelNumber'], params['name'], params['quantity'],
                         params['weight'], params['weightFormat'], params['price'], params['priceFormat'], params['brandName'], "LAPTOP")

        print(params)
        self.ramSize = params['ramSize']
        self.ramFormat = params['ramFormat']
        self.processorType = params['processorType']
        self.numCores = params['numCores']
        self.hardDriveSize = params['hardDriveSize']
        self.hardDriveFormat = params['hardDriveFormat']
        self.containsCamera = params['containsCamera']
        self.isTouch = params['isTouch']
        self.batteryInfo = params['batteryInfo']
        self.os = params['os']
        self.size = params['size']
        self.sizeFormat = "inch"
