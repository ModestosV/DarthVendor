from backend.apps.v1.accounts.models import Client

class Administrator(Client):

    def __init__(self, id, email, password,
                 isAdmin, isLoggedIn, timeStamp,
                 firstname, lastname, address, username, phone):

        """Constructor"""
        
        super().__init__(id, email, password,
                 isAdmin, isLoggedIn, timeStamp)

        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phone = phone