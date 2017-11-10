from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class Desktop(ItemSpecification):

    # param dict should contain these keys: modelNumber, name, quantity,
    # weight, weightFormat, price, priceFormat, brandName,
    # ramSize, ramFormat, processorType, numCores,
    # hardDriveSize, hardDriveFormat, dx, dy, dz
    def __init__(self, params):

        """" Constructor """

        super().__init__(params['modelNumber'], params['name'], params['quantity'],
                         params['weight'], params['weightFormat'], params['price'], params['priceFormat'], params['brandName'], "DESKTOP")

        self.ramSize = params['ramSize']
        self.ramFormat = params['ramFormat']
        self.processorType = params['processorType']
        self.numCores = params['numCores']
        self.hardDriveSize = params['hardDriveSize']
        self.hardDriveFormat = params['hardDriveFormat']
        self.dx = params['dx']
        self.dy = params['dy']
        self.dz = params['dz']
        self.dimensionFormat = "cm"
