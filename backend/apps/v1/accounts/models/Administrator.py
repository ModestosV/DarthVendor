class Administrator(object):

    def __init__(self, id, username, password,
                 firstname, lastname, address, email, phone):

        """Constructor"""

        self.id = id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.phone = phone
