from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class MonitorDisplay(ItemSpecification):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName, size, sizeFormat):

        """Constructor"""

        super().__init__(modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName, type)

        self.size = size
        self.sizeFormat = sizeFormat
