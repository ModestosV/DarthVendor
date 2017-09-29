from ItemSpecification import ItemSpecification


class MonitorDisplay(ItemSpecification):

    """Constructor"""
    def __init__(self, modelNumber, weight, weightFormat, price, priceFormat, brandName, size):

        super().__init__(modelNumber, weight, weightFormat, price, priceFormat, brandName)
        self.size = size
