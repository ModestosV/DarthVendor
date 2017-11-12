from backend.apps.v1.accounts.models.Client import Client

class Customer(Client):

    def __init__(self, id=None, email=None, password=None,
                 isAdmin=None, isLoggedIn=None, timeStamp=None,
                 username=None, firstname=None, lastname=None, address=None, phone=None):

        """Constructor"""

        super().__init__(id, email, password,
                 isAdmin, isLoggedIn, timeStamp)

        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phone = phone

        self.purchaseController = None
