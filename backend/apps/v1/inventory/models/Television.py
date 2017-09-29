from ItemSpecification import ItemSpecification


class Television(ItemSpecification):

    """Constructor"""

    def __init__(self, modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName, dimension, tvType):

        super().__init__(modelNumber, name, quantity, weight, weightFormat, price, priceFormat, brandName)

        self.dimension = dimension
        self.tvType = tvType
