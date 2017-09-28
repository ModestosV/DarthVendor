from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database


class Command(BaseCommand):
    help = 'Create television table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            CREATE TABLE television (
                id integer PRIMARY KEY AUTOINCREMENT,
                tvType string NOT NULL,
                dimensionFormat string NOT NULL,
                dx integer NOT NULL,
                dy integer NOT NULL,
                dz integer NOT NULL,
                FOREIGN KEY(televisionitem) REFERENCES item(id)
            );
        """

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)  

        connection.commit()
        connection.close()
