from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create item table'

    def handle(self, *args, **options):

        with Database() as cursor:
            query = """
                CREATE TABLE item (
                    quantity integer NOT NULL,
                    name varchar(255) NOT NULL,
                    weight double NOT NULL,
                    weightFormat varchar(255) NOT NULL,
                    price double NOT NULL,
                    priceFormat varchar(255) NOT NULL,
                    brandName varchar(255) NOT NULL,
                    type varchar(255) NOT NULL,
                    modelNumber varchar(255) NOT NULL,
                    PRIMARY KEY (type, modelNumber)
                );
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
