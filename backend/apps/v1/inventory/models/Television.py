from ItemSpecification import ItemSpecification


class Television(ItemSpecification):

    """Constructor"""
    def __init__(self, dimension, type):

        super(self, modelNumber, weight, weightFormat, price, priceFormat, brandName).__init__()
        self.dimension = dimension
        self.type = type
