from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class MonitorDisplay(ItemSpecification):

    # params should contain the following keys: modelNumber, name, quantity,
    # weight, weightFormat, price, priceFormat, brandName, size, sizeFormat
    def __init__(self, params):

        """Constructor"""

        super().__init__(params['modelNumber'], params['name'], params['quantity'],
                         params['weight'], params['weightFormat'], params['price'],
                         params['priceFormat'], params['brandName'], "MONTIORDISPLAY")

        self.size = params['size']
        self.sizeFormat = "inch"
