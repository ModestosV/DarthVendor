from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database


class Command(BaseCommand):
    help = 'Populate admin table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            INSERT INTO administrator (username, password)
            VALUES (                
                'foobar',
                'D4rthV3nD0r'
            );
        """

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)    

        connection.commit()
        connection.close()
