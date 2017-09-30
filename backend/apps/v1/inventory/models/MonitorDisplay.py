from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class MonitorDisplay(ItemSpecification):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName, size):

        """Constructor"""

        super().__init__(self, modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName)

        self.size = size
