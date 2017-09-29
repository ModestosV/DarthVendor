from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class MonitorDisplay(ItemSpecification):

    """Constructor"""
    def __init__(self, size):

        super().__init__(modelNumber, weight, weightFormat, price, priceFormat, brandName)
        self.size = size
