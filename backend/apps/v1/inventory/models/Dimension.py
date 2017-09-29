class Dimension(object):

    """Constructor"""
    def __init__(self, x, y, z, format="cm"):

        self.x = x
        self.y = y
        self.z = z
        self.format = format

        def getFormat(self):
            return self.format
