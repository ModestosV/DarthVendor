from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create cart table'

    def handle(self, *args, **options):

        with Database() as cursor:

            query = """
                CREATE TABLE cart (
                    cartID integer(11) NOT NULL,
                    userID integer(11) NOT NULL,
                    status varchar(255) NOT NULL,
                    total double NOT NULL,
                    totalFormat varchar(255) NOT NULL,
                    timeStamp datetime DEFAULT '',
                    PRIMARY KEY (cartID),
                    FOREIGN KEY (userID) REFERENCES user (id)
                );
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
