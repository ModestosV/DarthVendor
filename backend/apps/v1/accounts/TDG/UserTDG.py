from backend.utils.database import Database

class UserTDG:

    @staticmethod
    def insert(customer):

        with Database() as cursor:
            query = """
                INSERT INTO user (username, firstname, lastname, email, address, phone, password)
                VALUES ('{username}', '{firstname}', '{lastname}', '{email}',
                        '{address}', '{phone}', '{password}');
            """.format(**(customer.__dict__))

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    @staticmethod
    def update(user):

        with Database() as cursor:
            query = """
                UPDATE user SET
                isAdmin = {isAdmin},
                isLoggedIn = {isLoggedIn},
                timeStamp = '{timeStamp}'
                WHERE id = {id};
            """.format(**(user.__dict__))

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    @staticmethod
    def findUser(username):

        with Database() as cursor:
            query = """
                SELECT *
                FROM user 
                WHERE username = '{}';
            """

            try:
                cursor.execute(query)
                resultSet = cursor.fetchone()
                    return resultSet
            except Exception as error:
                print(error)
                return None

    @staticmethod
    def findEmail(email):

        with Database() as cursor:
            query = """
                SELECT *
                FROM user 
                WHERE email = '{}';
            """

            try:
                cursor.execute(query)
                resultSet = cursor.fetchone()
                    return resultSet
            except Exception as error:
                print(error)
                return None