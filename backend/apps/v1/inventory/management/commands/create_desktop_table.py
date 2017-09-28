from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database


class Command(BaseCommand):
    help = 'Create desktop table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            CREATE TABLE desktop (
                id integer PRIMARY KEY AUTOINCREMENT,
                ramSize integer NOT NULL,
                ramFormat string NOT NULL,
                processorType string NOT NULL,
                numCores integer NOT NULL,
                hardDriveSize integer NOT NULL,
                hardDriveFormat string NOT NULL,
                dx integer NOT NULL,
                dy integer NOT NULL,
                dz integer NOT NULL,
                dimensionFormat string NOT NULL,
                FOREIGN KEY(desktopitem) REFERENCES item(id)
            );
        """

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)  

        connection.commit()
        connection.close()
