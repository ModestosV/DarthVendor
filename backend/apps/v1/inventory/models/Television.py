from ItemSpecification import ItemSpecification


class Television(ItemSpecification):

    """Constructor"""
    def __init__(self, weight, weightFormat, price, priceFormat, brandName, dimension, tvType):

        super().__init__(modelNumber, weight, weightFormat, price, priceFormat, brandName)
        self.dimension = dimension
        self.type = tvType
