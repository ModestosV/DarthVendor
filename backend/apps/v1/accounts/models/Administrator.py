class Administrator(object):

	"""Constructor"""
    def __init__(self, id, username, password, firstname, lastname, address, email, phone):
		
        self.id = id
		self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.phone = phone
		
	
	def getUsername(self):
		
        return self.username
		
	
	def getPassword(self):
		
        return self.password