from django.conf import settings
from django.core.management.base import BaseCommand
from sqlite3 import dbapi2 as Database


class Command(BaseCommand):
    help = 'Create admin table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            CREATE TABLE administrator (
                id integer PRIMARY KEY AUTOINCREMENT,
                username varchar(255) UNIQUE,
                firstname varchar(255) DEFAULT '',
                lastname varchar(255) DEFAULT '',
                email varchar(255) DEFAULT '',
                address varchar(255) DEFAULT '',
                phone varchar(255) DEFAULT '',
                password varchar(255)
            );
        """

        try:
            cursor.execute(query)
        except Exception as error:
            print(error)

        connection.commit()
        connection.close()
