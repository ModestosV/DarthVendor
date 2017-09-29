class ItemSpecification(object):

    """Constructor"""
    def __init__(self, modelNumber, quantity, weight, weightFormat, price, priceFormat, brandName):

        self.modelNumber = modelNumber
        self.quantity = quantity
        self.weight = weight
        self.weightFormat = weightFormat
        self.price = price
        self.priceFormat = priceFormat
        self.brandName = brandName
