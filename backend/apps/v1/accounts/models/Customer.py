from backend.apps.v1.accounts.models import Client

class Customer(Client):

    def __init__(self, id, username, password,
                 isAdmin, isLoggedIn, timeStamp,
                 firstname, lastname, address, email, phone):

        """Constructor"""
        
        super().__init__(id, username, password,
                 isAdmin, isLoggedIn, timeStamp)

        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.phone = phone