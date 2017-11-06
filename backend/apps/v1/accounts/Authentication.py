from backend.apps.v1.accounts.models import Customer
from backend.apps.v1.accounts.models import Administrator
from backend.apps.v1.accounts.models import Client
from backend.apps.v1.accounts.TDG import UserMapper
import datetime

class Authentication:

    @staticmethod
    def register(customer):

        if(UserMapper.validUsernameToRegister(customer.username)):
            if(UserMapper.validEmailToRegister(customer.email)):
                return UserMapper.insert(customer)
            else:
                return False
        else:
            return False

    @staticmethod
    def islogged(client):

        if(client.isLoggedIn is 1):
            return True
        else:
            return False

    @staticmethod
    def login(client, isAdmin):

        if(client.isLoggedIn is 0):
        	client.isAdmin = isAdmin
            client.isLoggedIn = 1
            client.timeStamp = datetime.datetime.now()

            try:
                UserTDG.update(client)
            except Exception as error:
                print(error)
        else:
        	print("User has logged in.")

    
    @staticmethod
    def logout(client):

        if(client.isLoggedIn is 1):
            client.isLoggedIn = 0
            client.timeStamp = None

            try:
                UserTDG.update(client)
            except Exception as error:
                print(error)
        else:
        	print("User has already logged out.")