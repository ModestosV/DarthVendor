from backend.utils.database import Database

class UserTDG:

    @staticmethod
    def insert(customer):

        with Database() as cursor:
            query = """
                INSERT INTO user (email, password, isAdmin, isLoggedIn, username, firstname, lastname, address, phone)
                VALUES ('{email}', '{password}', 0, 0, '{username}', '{firstname}', '{lastname}',
                        '{address}', '{phone}');
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
                isLoggedIn = {isLoggedIn},
                timeStamp = '{timeStamp}'
                WHERE id = {id};
            """.format(**(user.__dict__))

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)

    @staticmethod
    def delete(userid):

        with Database() as cursor:

            try:
                cursor.execute("DELETE FROM user WHERE id = " + str(userid) + ";")
            except Exception as error:
                print(error)

    def findUser(useremail):

        with Database() as cursor:

            try:
                query = "SELECT * FROM user WHERE email = '{}';".format(useremail)
                cursor.execute(query)
                resultSet = cursor.fetchone()
                return resultSet
            except Exception as error:
                print(error)
                return None

    def findUsers():

        with Database() as cursor:

            try:
                cursor.execute("SELECT * FROM user WHERE isAdmin=0;")
                resultSet = cursor.fetchall()
                return resultSet
            except Exception as error:
                print(error)
                return None
