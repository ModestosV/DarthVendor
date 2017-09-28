from AbstractComputer import AbstractComputer


class Desktop(AbstractComputer):

    """Constructor"""
    def __init__(self, modelNumber, dimension):
        super().__init__()
        self.modelNumber = modelNumber
        self.dimension = dimension
