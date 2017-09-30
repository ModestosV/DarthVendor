from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create television table'

    def handle(self, *args, **options):

        with Database() as cursor:

            query = """
                CREATE TABLE television (
                    modelNumber varchar(255) NOT NULL,
                    tvType varchar(255) NOT NULL,
                    dimensionFormat varchar(255) NOT NULL,
                    dx double NOT NULL,
                    dy double NOT NULL,
                    dz double NOT NULL,
                    PRIMARY KEY (modelNumber),
                    FOREIGN KEY (modelNumber) REFERENCES item (modelNumber)
                );
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
