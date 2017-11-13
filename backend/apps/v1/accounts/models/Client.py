class Client(object):

    def __init__(self, id = None, email = None, password = None,
                 isAdmin = None, isLoggedIn = None, timeStamp = None):

        """Constructor"""

        self.id = id
        self.email = email
        self.password = password
        self.isAdmin = isAdmin
        self.isLoggedIn = isLoggedIn
        self.timeStamp = timeStamp