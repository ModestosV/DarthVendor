from backend.apps.v1.accounts.models.Customer import Customer
from backend.apps.v1.accounts.models.Client import Client
from backend.apps.v1.accounts.mapper.UserMapper import UserMapper
import datetime

class Authentication:

    @staticmethod
    def register(customer):

        if(UserMapper.validEmailToRegister(customer.email)):
            UserMapper.insert(customer)
            return True
        else:
            return False

    def login(client):

        if(UserMapper.existUser(client.email) is True):
            user = UserMapper.find(client.email)
            if(client.password == user.password):
                if(user.isLoggedIn is 0):
                    user.isAdmin = client.isAdmin
                    user.isLoggedIn = 1
                    client.timeStamp = datetime.datetime.now()

                    try:
                        UserMapper.update(user)
                        return user
                    except Exception as error:
                        print(error)
                else:
                    print("User has logged in.")
                    return None
            else:
                print("Password does not match.")
                return None
        else:
            print("User does not exist.")
            return None

    
    @staticmethod
    def logout(client):

        if(client.isLoggedIn is 1):
            client.isLoggedIn = 0
            client.timeStamp = None

            try:
                UserMapper.update(client)
            except Exception as error:
                print(error)
        else:
            print("User has already logged out.")