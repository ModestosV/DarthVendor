from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create token table'

    def handle(self, *args, **options):

        with Database() as cursor:

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
