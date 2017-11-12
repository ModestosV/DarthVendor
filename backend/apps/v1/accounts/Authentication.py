"""from backend.apps.v1.accounts.models.Customer import Customer
from backend.apps.v1.accounts.models.Client import Client"""
from backend.apps.v1.accounts.mapper.UserMapper import UserMapper
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import datetime

class Authentication:

    @staticmethod
    def register(customer):

        if(UserMapper.validEmailToRegister(customer.email)):
            customer.password = make_password(customer.password)
            UserMapper.insert(customer)
            return True
        else:
            return False

    def customerLogin(customer):

        if(UserMapper.existUser(customer.email) is True):
            user = UserMapper.findCustomer(customer.email)

            if(check_password(customer.password, user.password)):
                if(user.isLoggedIn is 0):
                    user.isLoggedIn = 1
                    customer.timeStamp = datetime.datetime.now()

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

    def adminLogin(admin):

        if(UserMapper.existUser(admin.email) is True):
            user = UserMapper.findAdmin(admin.email)
            if(user.isAdmin == 1):
                if(check_password(admin.password, user.password)):
                    if(user.isLoggedIn is 0):
                        user.isLoggedIn = 1
                        admin.timeStamp = datetime.datetime.now()

                        try:
                            UserMapper.update(user)
                            return user
                        except Exception as error:
                            print(error)
                    else:
                        print("Administrator has logged in.")
                        return None
                else:
                    print("Password does not match.")
                    return None
            else:
                print("Only Administrator can log in.")
                return None
        else:
            print("Administrator does not exist.")
            return None

    
    @staticmethod
    def logout(user):

        if(user.isLoggedIn is 1):
            user.isLoggedIn = 0
            user.timeStamp = None

            try:
                UserMapper.update(user)
            except Exception as error:
                print(error)
        else:
            print("User has already logged out.")


    @staticmethod
    def deleteCustomer(user):
        if(user.isAdmin == 0):
            UserMapper.delete(user)
            print("Your account is now removed.")
        else:
            print("Admin account cannot be removed.")

    @staticmethod
    def viewAllCustomer(user):
        if(user.isAdmin == 1):
            UserMapper.displayAllCustomer()
        else:
            print("Only Admin can see all the customers.")