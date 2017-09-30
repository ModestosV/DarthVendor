from django.conf import settings
from django.core.management.base import BaseCommand
from sqlite3 import dbapi2 as Database
from django.contrib.auth.hashers import make_password


FIRSTNAME = 'foo'
LASTNAME = 'bar'
USERNAME = 'foobar'
EMAIL = 'foobar@darthvendor.com'
PASSWORD = 'D4rthV3nD0r'


class Command(BaseCommand):
    help = 'Populate admin table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            INSERT INTO administrator (username, firstname, lastname, email, password)
            VALUES ('{}', '{}', '{}', '{}', '{}');
        """.format(USERNAME, FIRSTNAME, LASTNAME, EMAIL, make_password(PASSWORD))

        try:
            cursor.execute(query)
        except Exception as error:
            print(error)

        connection.commit()
        connection.close()
