from django.conf import settings
from django.core.management.base import BaseCommand
from sqlite3 import dbapi2 as Database
from django.contrib.auth.hashers import make_password


FIRSTNAME = 'foo'
LASTNAME = 'bar'
USERNAME = 'foobar'
EMAIL = 'foobar@darthvendor.com'
PASSWORD = 'D4rthV3nD0r'
ISADMIN = 1


class Command(BaseCommand):
    help = 'Populate user table with 1 admin'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            INSERT INTO user (username, firstname, lastname, email, password, isAdmin)
            VALUES ('{}', '{}', '{}', '{}', '{}', {});
        """.format(USERNAME, FIRSTNAME, LASTNAME, EMAIL, make_password(PASSWORD), ISADMIN)

        try:
            cursor.execute(query)
        except Exception as error:
            print(error)

        connection.commit()
        connection.close()
