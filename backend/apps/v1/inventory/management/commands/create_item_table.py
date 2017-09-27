from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database


class Command(BaseCommand):
    help = 'Create item table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            CREATE TABLE item (
                id integer PRIMARY KEY AUTOINCREMENT,
                quantity integer NOT NULL,
                weight double NOT NULL,
                weightFormat string NOT NULL,
                price double NOT NULL,
                priceFormat string NOT NULL,
                //brandName string NOT NULL,
                type string NOT NULL,
                modelNumber integer UNIQUE NOT NULL
            );
        """

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)  

        connection.commit()
        connection.close()
