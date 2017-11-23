from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.utils.database import Database
from backend.apps.v1.accounts.serializers.user import UserSerializer
from backend.apps.v1.accounts.TDG.UserTDG import UserTDG
from backend.apps.v1.accounts.mapper.UserMapper import UserMapper
from backend.apps.v1.accounts.models.Customer import Customer
from backend.apps.v1.accounts.models.Administrator import Administrator

from backend.apps.v1.accounts.Authentication import Authentication

class Test_View(APIView):
    """
        API: users/
    """

    def get(self, request):

        """cus = Customer(0,"555@gmail.com","55555",0,0,0,"tt","ttt","ttt","555 St catherine","5155555555")
        UserTDG.insert(cus)"""
        Authentication.deleteCustomer("555@gmail.com")

        """resultSet = UserTDG.findUser("555@gmail.com")
        
        user = Customer("","","",0,0,"","","","","","")
        if(not resultSet):
            print("found nothing")
        else:
            for row in resultSet:
                user.id = row["id"]
                user.email = row["email"]
                user.password = row["password"]
                user.isAdmin = row["isAdmin"]
                user.isLoggedIn = row["isLoggedIn"]
            print(user.id)

        user.isLoggedIn=0"""

        """UserTDG.update(user)"""

        """UserTDG.delete(10)

        resultSet = UserTDG.findUsers()
        
        if(not resultSet):
            print("found nothing")
        else:
            for row in resultSet:
                print("User id: " + str(row['id']))
                print("Email: " + row['email'])
                print("Username: " + row['username'])
                print("Firstname: " + row['firstname'])
                print("Lastname: " + row['lastname'])
                print("Address: " + row['address'])
                print("Phone: " + row['phone'])
                print("is logged: " + str(row['isLoggedIn']))
                print("")"""

        """valid = UserMapper.validEmailToRegister("1111@gmail.com")
        print(valid)"""
        
        """cus = Customer(0,"555@gmail.com","55555",0,0,0,"tt","ttt","ttt","555 St catherine","5155555555")
        UserMapper.insert(cus)"""
        

        """valid = UserMapper.existUser("11111@gmail.com")
        print(valid)"""

        """user = UserMapper.findAdmin("foobar@darthvendor.com")
        print(user.username)
        print(user.isLoggedIn)
                        
        user.isLoggedIn = 0
        valid = UserMapper.update(user)
        user1 = UserMapper.findAdmin("1111@gmail.com")
        print(user.username)
        print(user1.isLoggedIn)"""
        
        """user = UserMapper.findAdmin("foobar@darthvendor.com")
        print(user.username)
        print(user.isLoggedIn)
                        
        user.isLoggedIn = 0

        UserMapper.update(user)
        valid = UserMapper.isLoggedCustomer("foobar@darthvendor.com")
        print(valid)"""

        """valid = UserMapper.existUser("555@gmail.com")
        print(valid)"""
        """user = UserMapper.findAdmin("555@gmail.com")
        print(user.username)"""
        """UserMapper.delete(user)
        valid = UserMapper.existUser("555@gmail.com")
        print(valid)"""
        """UserMapper.displayAllCustomer()"""
        """cus = Customer(0,"555@gmail.com","55555",0,0,0,"tt","ttt","ttt","555 St catherine","5155555555")
        Authentication.register(cus)"""

        """UserMapper.displayAllCustomer()"""
        """cus = Customer(0,"foobar@darthvendor.com",make_password"D4rthV3nD0r",0,0,0,"","","","","")
        user = Authentication.adminLogin(cus)"""
        """print(user.username)"""
        """Authentication.logout(user)"""
        """print(user.isLoggedIn)"""
        """cus = Customer(0,"555@gmail.com","55555",0,0,0,"tt","ttt","ttt","555 St catherine","5155555555")
        Authentication.register(cus)"""
        """cus = Customer(0,"foobar@darthvendor.com","D4rthV3nD0r",0,0,0,"","","","","")"""
        """user = UserMapper.findAdmin("foobar@darthvendor.com")"""
        """user = Authentication.adminLogin(cus)"""
        """print(user.username)"""
        """Authentication.logout(user)"""
        """Authentication.deleteCustomer(user)"""
        """Authentication.viewAllCustomer(user)"""
        return Response()
