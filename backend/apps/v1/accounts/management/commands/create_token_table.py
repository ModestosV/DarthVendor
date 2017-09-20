from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database


class Command(BaseCommand):
    help = 'Create token table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            CREATE TABLE token (
                id integer PRIMARY KEY AUTOINCREMENT,
                token varchar(255) UNIQUE,
                admin_id integer UNIQUE,                
                FOREIGN KEY (admin_id) REFERENCES administrator(id)
            );
        """

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)  

        connection.commit()
        connection.close()
