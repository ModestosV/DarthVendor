from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create user table'

    def handle(self, *args, **options):

        with Database() as cursor:

            query = """
                CREATE TABLE user (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    username varchar(255) UNIQUE,
                    firstname varchar(255) DEFAULT '',
                    lastname varchar(255) DEFAULT '',
                    email varchar(255) UNIQUE DEFAULT '',
                    address varchar(255) DEFAULT '',
                    phone varchar(255) DEFAULT '',
                    password varchar(255),
                    isAdmin tinyint(1) DEFAULT 0,
                    isActivated tinyint(1) DEFAULT 1,
                    timeStamp datetime DEFAULT ''
                );
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
