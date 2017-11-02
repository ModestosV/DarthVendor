from backend.apps.v1.accounts.models import Customer
from backend.apps.v1.accounts.models import Administrator
from backend.apps.v1.accounts.models import Client
from backend.apps.v1.accounts.TDG import UserTDG

class UserMapper:

    @staticmethod
    def validUsernameToRegister(username):

        resultSet = UserTDG.findUser(username);

        if(resultSet.rowcount() is 0):
        	return True
        else:
        	return False

    @staticmethod
    def validEmailToRegister(email):

        resultSet = UserTDG.findEmail(email);

        if(resultSet.rowcount() is 0):
            return True
        else:
            return False

    @staticmethod
    def insert(customer):

        try:
            UserTDG.insert(customer)
            return True
        except Exception as error:
            print(error)
            return False

    @staticmethod
    def existUser(username):

        resultSet = UserTDG.findUser(username);

        if(resultSet.rowcount() is 0):
            return False
        else:
            return True

    @staticmethod
    def find(username):

        resultSet = UserTDG.findUser(username);

        user = Client()
        
        for row in resultSet:
        	user.id = row['id']
            user.username = row['username']
            user.password = row['password']
            user.isAdmin = row['isAdmin']
            user.isLoggedIn = row['isLoggedIn']
            user.timeStamp = row['timeStamp']

        return user

    @staticmethod
    def update(client):

        try:
            UserTDG.update(client)
            return True
        except Exception as error:
            print(error)
            return False        