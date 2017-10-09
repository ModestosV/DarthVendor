from django.core.management.base import BaseCommand
from backend.utils.database import Database
from django.contrib.auth.hashers import make_password


users = [
    dict(
        firstname='foo',
        lastname='bar',
        username='foobar',
        email='foobar@darthvendor.com',
        password=make_password('D4rthV3nD0r'),
        isAdmin=1
    ),
    dict(
        firstname='lorem',
        lastname='ipsum',
        username='client',
        email='client@loremipsum.com',
        password=make_password('01010101'),
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
