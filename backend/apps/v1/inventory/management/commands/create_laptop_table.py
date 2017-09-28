from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database


class Command(BaseCommand):
    help = 'Create desktop table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            CREATE TABLE laptop (
                id integer PRIMARY KEY AUTOINCREMENT,
                ramSize integer NOT NULL,
                ramFormat string NOT NULL,
                processorType string NOT NULL,
                numCores integer NOT NULL,
                hardDriveSize integer NOT NULL,
                hardDriveFormat integer NOT NULL,
                containsCamera string NOT NULL,
                isTouch string NOT NULL,
                batteryInfo string NOT NULL,
                os string NOT NULL,
                size integer NOT NULL,
                sizeFormat string NOT NULL,
                FOREIGN KEY(laptopitem) REFERENCES item(id)
            );
        """

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)  

        connection.commit()
        connection.close()
