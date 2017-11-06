from backend.apps.v1.accounts.models.Customer import Customer
from backend.apps.v1.accounts.models.Client import Client
from backend.apps.v1.accounts.TDG.UserTDG import UserTDG

class UserMapper:

    def validEmailToRegister(email):

        resultSet = UserTDG.findUser(email)

        if not resultSet:
            return True
        else:
            return False

    @staticmethod
    def insert(customer):

        try:
            UserTDG.insert(customer)
        except Exception as error:
            print(error)

    @staticmethod
    def existUser(email):

        resultSet = UserTDG.findUser(email)

        if not resultSet:
            return False
        else:
            return True

    @staticmethod
    def find(email):

        resultSet = UserTDG.findUser(email)

        user = Client("","","",0,0,"")
        
        for row in resultSet:
            user.id = row['id']
            user.email = row['email']
            user.password = row['password']
            user.isAdmin = row['isAdmin']
            user.isLoggedIn = row['isLoggedIn']
            user.timeStamp = row['timeStamp']

        return user

    @staticmethod
    def update(client):

        try:
            UserTDG.update(client)
        except Exception as error:
            print(error)

    @staticmethod
    def isLogged(email):

        user = UserMapper.find(email)
        if(user.isLoggedIn is 1):
            return True
        else:
            return False