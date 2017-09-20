from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database, OperationalError


class Command(BaseCommand):
    help = 'Create admin table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            CREATE TABLE administrator(
                id integer PRIMARY KEY AUTOINCREMENT,
                username varchar(255),
                password varchar(255)
            );
        """

        try:
            cursor.execute(query)                
        except OperationalError as error:
            print(error)

        connection.commit()
        connection.close()
