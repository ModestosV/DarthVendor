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
        firstname='admini',
        lastname='adi',
        username='admini',
        email='admin1@gmail.com',
        password=make_password('admin'),
        isAdmin=1
    ),
    
    dict(
        firstname='adminii',
        lastname='adii',
        username='adminii',
        email='admin2@gmail.com',
        password=make_password('admin'),
        isAdmin=1
    ),    

    dict(
        firstname='client',
        lastname='',
        username='client',
        email='client1@email.com',
        password=make_password('client'),
        isAdmin=0
    ),
    
    dict(
        firstname='clientii',
        lastname='',
        username='clientii',
        email='client2@email.com',
        password=make_password('client'),
        isAdmin=0
    ),
    
    dict(
        firstname='clientiii',
        lastname='',
        username='clientiii',
        email='client3@email.com',
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
