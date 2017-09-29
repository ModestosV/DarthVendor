from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class MonitorDisplay(ItemSpecification):

    """Constructor"""
    def __init__(self, name, modelNumber, weight, weightFormat, price, priceFormat, brandName, size):

        super().__init__(modelNumber, name, weight, weightFormat, price, priceFormat, brandName)
        self.size = size
