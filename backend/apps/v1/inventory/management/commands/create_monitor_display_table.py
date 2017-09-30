from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create monitor display table'

    def handle(self, *args, **options):

        with Database() as cursor:
            query = """
                CREATE TABLE monitorDisplay (
                    modelNumber varchar(255) NOT NULL,
                    size double NOT NULL,
                    sizeFormat varchar(255) NOT NULL,
                    PRIMARY KEY (modelNumber),
                    FOREIGN KEY (modelNumber) REFERENCES item (modelNumber)
                );
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
