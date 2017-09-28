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
                modelNumber string NOT NULL,
                size double NOT NULL,
                sizeFormat string NOT NULL,
                PRIMARY KEY (modelNumber),
                FOREIGN KEY (modelNumber) REFERENCES item (modelNumber)
            );
        """

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)  

        connection.commit()
        connection.close()
