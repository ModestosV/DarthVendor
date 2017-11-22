class Client(object):

    def __init__(self, id = None, email = None, password = None,
                 isAdmin = None, isActivated = None, timeStamp = None):

        """Constructor"""

        self.id = id
        self.email = email
        self.password = password
        self.isAdmin = isAdmin
        self.isActivated = isActivated
        self.timeStamp = timeStamp