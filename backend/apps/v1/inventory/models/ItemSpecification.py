class ItemSpecification(object):

    def __init__(self, modelNumber, name, quantity,
                 weight, weightFormat, price, priceFormat, brandName, type):

        """Constructor"""

        self.modelNumber = modelNumber
        self.name = name
        self.quantity = quantity
        self.weight = weight
        self.weightFormat = weightFormat
        self.price = price
        self.priceFormat = priceFormat
        self.brandName = brandName
        self.type = type
