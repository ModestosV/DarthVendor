from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database

#Test Values
QUANTITY = 5
WEIGHT = 10.0
WEIGHTFORMAT = 'lbs'
PRICE = 9.99
PRICEFORMAT = 'CAD'
BRANDNAME = 'SONY'
NAME = 'Modestos'
TYPE = 'TV'
MODELNUMBER = 'x123123'

class Command(BaseCommand):
    help = 'Populate item table';

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            INSERT INTO item (quantity, name, weight, weightFormat, price, 
                priceFormat, brandName, type, modelNumber)
            VALUES (                
                {},
                '{}',
                {},
               '{}',
                {},
               '{}',
               '{}',
               '{}',
               '{}'
            );
        """.format(QUANTITY, NAME, WEIGHT, WEIGHTFORMAT, PRICE, 
            PRICEFORMAT, BRANDNAME, TYPE, MODELNUMBER)
        print()
        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)    

        connection.commit()
        connection.close()
