from django.core.management.base import BaseCommand
from backend.utils.database import Database


televisions = [
    dict(
        quantity=10,
        weight=100.0,
        weightFormat='lbs',
        price=5299.99,
        priceFormat='CAD',
        brandName='SAMSUNG',
        name='Curve TV',
        type='television',
        modelNumber='VVVVVVV',
        tvType='OLED',
        dx=80,
        dy=100,
        dz=5,
        dimensionFormat='INCH',
    ),
    dict(
        quantity=2,
        weight=50.0,
        weightFormat='lbs',
        price=1599.85,
        priceFormat='CAD',
        brandName='SAMSUNG',
        name='Thin TV',
        type='TELEVISION',
        modelNumber='THINTHINTHIN',
        tvType='OLED',
        dx=50,
        dy=30,
        dz=2,
        dimensionFormat='INCH',
    )
]


class Command(BaseCommand):
    help = 'Populate television table'

    def handle(self, *args, **options):

        with Database() as cursor:

            for television in televisions:
                query = """
                    INSERT INTO item (quantity, name, weight, weightFormat, price,
                        priceFormat, brandName, type, modelNumber)
                    VALUES ({quantity}, '{name}', {weight}, '{weightFormat}', 
                        {price}, '{priceFormat}', '{brandName}', '{type}', '{modelNumber}');
                """.format(**television)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

                query = """
                    INSERT INTO television (modelNumber, tvType,
                        dx, dy, dz, dimensionFormat)
                    VALUES ('{modelNumber}', '{tvType}',
                        {dx}, {dy}, {dz}, '{dimensionFormat}');
                """.format(**television)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)
