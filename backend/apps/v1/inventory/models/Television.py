from backend.apps.v1.inventory.models.ItemSpecification import ItemSpecification


class Television(ItemSpecification):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName,
                 dimension, tvType):

        """Constructor"""

        super().__init__(self, modelNumber, name, quantity,
                         weight, weightFormat, price, priceFormat, brandName)

        self.dimension = dimension
        self.tvType = tvType
