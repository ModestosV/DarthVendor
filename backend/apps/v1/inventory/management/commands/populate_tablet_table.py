from django.core.management.base import BaseCommand
from backend.utils.database import Database


tablets = [
    dict(
        quantity=5,
        weight=10.0,
        weightFormat='lbs',
        price=299.99,
        priceFormat='CAD',
        brandName='SAMSUNG',
        name='Galaxy Tab S2',
        type='tablet',
        modelNumber='GGGGGG',
        ramSize=16,
        ramFormat='GB',
        processorType='ARM',
        numCores=2,
        hardDriveSize=128,
        hardDriveFormat='GB',
        os='Android',
        batteryInfo='3000mAH',
        dx=10,
        dy=10,
        dz=1.5,
        dimensionFormat='CM',
        cameraInfo='10.2 MP',
        size=12.5,
        sizeFormat='PX'

    ),
    dict(
        quantity=10,
        weight=5.0,
        weightFormat='lbs',
        price=699.99,
        priceFormat='CAD',
        brandName='APPLE',
        name='Ipad Pro',
        type='tablet',
        modelNumber='AAAAAAAA',
        ramSize=16,
        ramFormat='GB',
        processorType='APPLE',
        numCores=4,
        hardDriveSize=512,
        hardDriveFormat='GB',
        os='iOS',
        batteryInfo='6000mAH',
        dx=20,
        dy=20,
        dz=1,
        dimensionFormat='INCH',
        cameraInfo='15.5 MP',
        size=20.5,
        sizeFormat='PX'
    )
]


class Command(BaseCommand):
    help = 'Populate tablet table'

    def handle(self, *args, **options):

        with Database() as cursor:

            for tablet in tablets:
                query = """
                    INSERT INTO item (quantity, name, weight, weightFormat, price,
                        priceFormat, brandName, type, modelNumber)
                    VALUES ({quantity}, '{name}', {weight}, '{weightFormat}', 
                        {price}, '{priceFormat}', '{brandName}', '{type}', '{modelNumber}');
                """.format(**tablet)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

                query = """
                    INSERT INTO tablet (modelNumber, ramSize, ramFormat,
                        processorType, numCores, hardDriveSize, hardDriveFormat,
                        os, batteryInfo, dx, dy, dz, dimensionFormat, cameraInfo,
                        size, sizeFormat)
                    VALUES ('{modelNumber}', {ramSize}, '{ramFormat}',
                        '{processorType}', {numCores}, {hardDriveSize}, '{hardDriveFormat}',
                        '{os}', '{batteryInfo}', {dx}, {dy}, {dz}, '{dimensionFormat}', '{cameraInfo}',
                        {size}, '{sizeFormat}');
                """.format(**tablet)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)
