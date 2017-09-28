from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)


#USERNAME = 'foobar'
#PASSWORD = 'D4rthV3nD0r'

#Test Values
QUANTITY = 5
WEIGHT = 10.0
WEIGHTFORMAT = 'lbs'
PRICE = 9.99
PRICEFORMAT = 'CAD'
BRANDFORMAT = 'TEST'
TYPE = 'TV'
MODELNUMBER = 123123

class Command(BaseCommand):
    help = 'Populate item table';

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            INSERT INTO item (quantity, weight,weightFormat,price, 
                priceFormat, brandFormat, type, 
                modelNumber)
            VALUES (                
                {},
                {},
                '{}',
                {},
                '{}',
                '{}',
                '{}',
                {}
            );
        """.format(QUANTITY, WEIGHT, WEIGHTFORMAT, PRICE, 
            PRICEFORMAT, BRANDFORMAT, TYPE, MODELNUMBER)
        print()
        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)    

        connection.commit()
        connection.close()
