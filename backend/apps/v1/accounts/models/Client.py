class Client(object):

    def __init__(self, id, username, password,
                 isAdmin, isLoggedIn, timeStamp):

        """Constructor"""

        self.id = id
        self.username = username
        self.password = password
        self.isAdmin = isAdmin
        self.isLoggedIn = isLoggedIn
        self.timeStamp = timeStamp