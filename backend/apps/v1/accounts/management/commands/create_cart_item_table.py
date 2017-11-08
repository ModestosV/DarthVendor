from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create cart item table'

    def handle(self, *args, **options):

        with Database() as cursor:

            query = """
                CREATE TABLE cartItem (
                    cartID integer(11) NOT NULL,
                    serialNum varchar(255) NOT NULL,
                    price double NOT NULL,
                    priceFormat varchar(255) NOT NULL,
                    PRIMARY KEY (cartID),
                    FOREIGN KEY (serialNum) REFERENCES cart (cartID)
                );
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
