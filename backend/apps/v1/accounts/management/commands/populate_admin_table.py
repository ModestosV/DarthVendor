from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)


USERNAME = 'foobar'
PASSWORD = 'D4rthV3nD0r'

class Command(BaseCommand):
    help = 'Populate admin table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            INSERT INTO administrator (username, password)
            VALUES (                
                '{}',
                '{}'
            );
        """.format(USERNAME, make_password(PASSWORD))

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)    

        connection.commit()
        connection.close()
