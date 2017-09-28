from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database


class Command(BaseCommand):
    help = 'Create monitor display table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            CREATE TABLE monitorDisplay (
                id integer PRIMARY KEY AUTOINCREMENT,
                size integer NOT NULL,
                sizeFormat string NOT NULL,
                FOREIGN KEY(monitoritem) REFERENCES item(id)
            );
        """

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)  

        connection.commit()
        connection.close()
