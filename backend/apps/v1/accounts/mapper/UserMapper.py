from backend.apps.v1.accounts.models.Customer import Customer
from backend.apps.v1.accounts.models.Administrator import Administrator
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
    def displayAllCustomer():
        resultSet = UserTDG.findUsers()
        
        customerList = list()
        if not resultSet:
            return None
        else:    
            for row in resultSet:
            
                cus = Customer({
                    'id': row.get('id'),
                    'email': row.get('email'),
                    'timeStamp': row.get('timeStamp'),
                    'username': row.get('username'),
                    'firstname': row.get('firstname'),
                    'lastname': row.get('lastname'),
                    'address': row.get('address'),
                    'phone': row.get('phone')
                })
                customerList.append(cus)

        return customerList

    @staticmethod
    def findCustomer(email):

        row = UserTDG.findUser(email)

        user = Customer(0, "", "", 0, 0, "", "", "", "", "", "")
        user.id = row['id']
        user.email = row['email']
        user.password = row['password']
        user.isAdmin = False
        user.isLoggedIn = row['isLoggedIn']
        user.timeStamp = row['timeStamp']
        user.username = row['username']
        user.firstname = row['firstname']
        user.lastname = row['lastname']
        user.address = row['address']
        user.phone = row['phone']

        return user

    @staticmethod
    def findAdmin(email):

        row = UserTDG.findUser(email)

        user = Administrator(0,"","",0,0,"","","","","","")

        user.id = row['id']
        user.email = row['email']
        user.password = row['password']
        user.isAdmin = True if row['isAdmin'] == 1 else False
        user.isLoggedIn = row['isLoggedIn']
        user.timeStamp = row['timeStamp']
        user.username = row['username']
        user.firstname = row['firstname']
        user.lastname = row['lastname']
        user.address = row['address']
        user.phone = row['phone']

        return user

    @staticmethod
    def update(user):

        try:
            UserTDG.update(user)
        except Exception as error:
            print(error)

    @staticmethod
    def delete(user):

        try:
            UserTDG.delete(user.id)
        except Exception as error:
            print(error)

    @staticmethod
    def isLoggedCustomer(email):

        user = UserMapper.findCustomer(email)
        if(user.isLoggedIn is 1):
            return True
        else:
            return False

    @staticmethod
    def isLoggedAdmin(email):

        user = UserMapper.findAdmin(email)
        if(user.isLoggedIn is 1):
            return True
        else:
            return False
