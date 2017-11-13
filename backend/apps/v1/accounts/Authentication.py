from backend.apps.v1.accounts.models.Customer import Customer
from backend.apps.v1.accounts.models.Client import Client
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

    @staticmethod
    def customerLogin(email, password):

        customer = UserMapper.findCustomer(email)

        if check_password(password, customer.password):
            return customer

        return None

    def adminLogin(email, password):

        admin = UserMapper.findAdmin(email)

        if admin.isAdmin is not True:
            return None

        if check_password(password, admin.password):
            return admin

        return None

    @staticmethod
    def deleteCustomer(user):
        if(user.isAdmin == 0):
            UserMapper.delete(user)
            print("Your account is now removed.")
        else:
            print("Admin account cannot be removed.")

    @staticmethod
    def viewAllCustomer(user):

        UserMapper.displayAllCustomer()