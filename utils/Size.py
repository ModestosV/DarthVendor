class Size(object):

	"""Constructor"""
    def __init__(self, size, format="inch"):
		
        self.size = size
		self.format = format
		
	def getFormat(self):

        return self.format	