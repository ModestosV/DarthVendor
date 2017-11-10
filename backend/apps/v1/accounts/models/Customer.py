from backend.apps.v1.accounts.models.Client import Client

class Customer(Client):

    def __init__(self, id, email, password,
                 isAdmin, isLoggedIn, timeStamp,
                 username, firstname, lastname, address, phone):

        """Constructor"""
        
        super().__init__(id, email, password,
                 isAdmin, isLoggedIn, timeStamp)

        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phone = phone