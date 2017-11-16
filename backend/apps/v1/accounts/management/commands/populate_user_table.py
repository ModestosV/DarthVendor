from django.core.management.base import BaseCommand
from backend.utils.database import Database
from django.contrib.auth.hashers import make_password

users = [
    dict(
        firstname='foo',
        lastname='bar',
        username='foobar',
        email='foobar@darthvendor.me',
        password=make_password('D4rthV3nD0r'),
        isAdmin=1
    ),

    dict(
        firstname='admin',
        lastname='test',
        username='admin',
        email='admin@darthvendor.me',
        password=make_password('admin'),
        isAdoyomin=1
    ),
    
    dict(
        firstname='constantinos',
        lastname='constantinides',
        username='cc',
        email='cc@cse.concordia.ca',
        password=make_password('admin'),
        isAdmin=1
    ),    

    dict(
        firstname='client',
        lastname='',
        username='client',
        email='client@email.com',
        password=make_password('client'),
        isAdmin=0
    ),
    
    dict(
        firstname='customer',
        lastname='',
        username='client',
        email='customer@email.com',
        password=make_password('client'),
        isAdmin=0
    ),
    
    dict(
        firstname='merchant',
        lastname='',
        username='client',
        email='merchant@email.com',
        password=make_password('client'),
        isAdmin=0
    )    
]


class Command(BaseCommand):
    help = 'Populate user table'

    def handle(self, *args, **options):

        with Database() as cursor:

            for user in users:      
                      
                query = """
                    INSERT INTO user (username, firstname, lastname, email, password, isAdmin)
                    VALUES ('{username}', '{firstname}', '{lastname}', '{email}', '{password}', {isAdmin});
                """.format(**user)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)
