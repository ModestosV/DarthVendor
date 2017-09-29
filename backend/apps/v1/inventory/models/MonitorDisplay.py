from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class MonitorDisplay(ItemSpecification):

    """Constructor"""
    def __init__(self, modelNumber, quantity, weight, weightFormat, price, priceFormat, brandName, size):

        super().__init__(modelNumber, quantity, weight, weightFormat, price, priceFormat, brandName)
        self.size = size
