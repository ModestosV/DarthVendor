from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create purchase collection table'

    def handle(self, *args, **options):

        with Database() as cursor:

            query = """
                CREATE TABLE purchaseCollection (
                    serialNum varchar(255) NOT NULL,
                    modelNum varchar(255) NOT NULL,
                    userID integer(11) NOT NULL,
                    type varchar(255) NOT NULL,
                    timeStamp datetime DEFAULT '',
                    PRIMARY KEY (serialNum),
                    FOREIGN KEY (userID) REFERENCES user (id)
                ); 
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
