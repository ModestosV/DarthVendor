from backend.apps.v1.accounts.models.Customer import Customer
from backend.apps.v1.accounts.models.Client import Client
from backend.apps.v1.accounts.mapper.UserMapper import UserMapper
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import datetime
from contracts import contract


class Authentication:
    
    @staticmethod
    @contract(returns='bool')
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
    @contract(returns='bool')
    def deleteCustomer(email):
            
        return UserMapper.updateActivation(email)

    @staticmethod
    @contract(returns='list|None')
    def viewAllCustomer():

        return UserMapper.displayAllCustomer()
