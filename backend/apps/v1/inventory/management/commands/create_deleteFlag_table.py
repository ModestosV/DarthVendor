from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create deleteFlag table'

    def handle(self, *args, **options):

        with Database() as cursor:

            query = """
                CREATE TABLE deleteFlag (
                    modelNumber varchar(255) NOT NULL,
                    type varchar(255) NOT NULL,
                    PRIMARY KEY (modelNumber)
                );
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
