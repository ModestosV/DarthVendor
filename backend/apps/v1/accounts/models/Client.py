class Client(object):

    def __init__(self, id, email, password,
                 isAdmin, isLoggedIn, timeStamp):

        """Constructor"""

        self.id = id
        self.email = email
        self.password = password
        self.isAdmin = isAdmin
        self.isLoggedIn = isLoggedIn
        self.timeStamp = timeStamp