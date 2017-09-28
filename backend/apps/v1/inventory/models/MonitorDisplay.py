from ItemSpecification import ItemSpecification


class MonitorDisplay(ItemSpecification):

    """Constructor"""
    def __init__(self, modelNumber, size):

        super().__init__
        self.modelNumber = modelNumber
        self.size = size
