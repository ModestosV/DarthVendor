from django.core.management.base import BaseCommand
from backend.utils.database import Database


desktops = [
    dict(
        quantity=46,
        weight=15.0,
        weightFormat='lbs',
        price=2299.99,
        priceFormat='CAD',
        brandName='RAZER',
        name='Razer Desktop',
        type='DESKTOP',
        modelNumber='ZZZZZZZ',
        ramSize=16,
        ramFormat='GB',
        processorType='INTEL',
        numCores=4,
        hardDriveSize=2,
        hardDriveFormat='TB',
        dx=15,
        dy=30,
        dz=1,
        dimensionFormat='INCH',
    ),
    dict(
        quantity=5,
        weight=17.0,
        weightFormat='lbs',
        price=2699.99,
        priceFormat='CAD',
        brandName='APPLE',
        name='Apple Desktop',
        type='desktop',
        modelNumber='PPPPPPPPPPPPP',
        ramSize=16,
        ramFormat='GB',
        processorType='APPLE',
        numCores=4,
        hardDriveSize=1,
        hardDriveFormat='TB',
        dx=20,
        dy=20,
        dz=1,
        dimensionFormat='INCH',
    )
]


class Command(BaseCommand):
    help = 'Populate desktop table'

    def handle(self, *args, **options):

        with Database() as cursor:

            for desktop in desktops:
                query = """
                    INSERT INTO item (quantity, name, weight, weightFormat, price,
                        priceFormat, brandName, type, modelNumber)
                    VALUES ({quantity}, '{name}', {weight}, '{weightFormat}', 
                        {price}, '{priceFormat}', '{brandName}', '{type}', '{modelNumber}');
                """.format(**desktop)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

                query = """
                    INSERT INTO desktop (modelNumber, ramSize, ramFormat,
                        processorType, numCores, hardDriveSize, hardDriveFormat,
                        dx, dy, dz, dimensionFormat)
                    VALUES ('{modelNumber}', {ramSize}, '{ramFormat}',
                        '{processorType}', {numCores}, {hardDriveSize}, '{hardDriveFormat}',
                        {dx}, {dy}, {dz}, '{dimensionFormat}');
                """.format(**desktop)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)
