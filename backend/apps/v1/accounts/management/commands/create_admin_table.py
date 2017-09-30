from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create admin table'

    def handle(self, *args, **options):

        with Database() as cursor:

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
