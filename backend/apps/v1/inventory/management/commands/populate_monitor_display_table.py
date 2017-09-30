from django.core.management.base import BaseCommand
from backend.utils.database import Database


monitors = [
    dict(
        quantity=5,
        weight=10.0,
        weightFormat='lbs',
        price=9.99,
        priceFormat='CAD',
        brandName='SONY',
        name='Gaming Monitor',
        type='monitor',
        modelNumber='x123131',
        size=30.5,
        sizeFormat='inch'
    ),
    dict(
        quantity=10,
        weight=5.0,
        weightFormat='lbs',
        price=19.99,
        priceFormat='CAD',
        brandName='SAMSUNG',
        name='Curve Display',
        type='monitor',
        modelNumber='x80942380942',
        size=50.5,
        sizeFormat='inch'
    )
]


class Command(BaseCommand):
    help = 'Populate monitor display table'

    def handle(self, *args, **options):

        with Database() as cursor:

            for monitor in monitors:
                query = """
                    INSERT INTO item (quantity, name, weight, weightFormat, price,
                        priceFormat, brandName, type, modelNumber)
                    VALUES ({quantity}, '{name}', {weight}, '{weightFormat}', 
                        {price}, '{priceFormat}', '{brandName}', '{type}', '{modelNumber}');
                """.format(**monitor)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

                query = """
                    INSERT INTO monitorDisplay (modelNumber, size, sizeFormat)
                    VALUES ('{modelNumber}', {size}, '{sizeFormat}');
                """.format(**monitor)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)
