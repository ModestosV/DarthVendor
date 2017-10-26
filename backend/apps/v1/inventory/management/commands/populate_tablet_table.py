from django.core.management.base import BaseCommand
from backend.utils.database import Database


tablets = [
    dict(
        modelNumber='GGGGGG',
        quantity=5,
        name='test',
        weight=10.0,
        weightFormat='lbs',
        price=299.99,
        priceFormat='CAD',
        brandName='SAMSUNG',
        type='tablet',
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
        modelNumber='GAGGGGG',
        quantity=50,
        name='test0',
        weight=11.0,
        weightFormat='lbs',
        price=2299.99,
        priceFormat='CAD',
        brandName='SAMSUNG',
        type='tablet',
        ramSize=16,
        ramFormat='GB',
        processorType='ARM',
        numCores=2,
        hardDriveSize=1284,
        hardDriveFormat='GB',
        os='Android',
        batteryInfo='300043mAH',
        dx=10,
        dy=10,
        dz=1.5,
        dimensionFormat='CM',
        cameraInfo='10.2 MP',
        size=12.5,
        sizeFormat='PX'
    )
]

tabletIDs = [
    dict(
        serialNum='f569g79874',
        modelNum='GGGGGG',
        isLocked=0
    ),
    dict(
        serialNum='bWERTERTERRK',
        modelNum='GAGGGGG',
        isLocked=0
    )
]


class Command(BaseCommand):
    help = 'Populate tablet table'

    def handle(self, *args, **options):

        with Database() as cursor:

            for tablet in tablets:
                query = """
                    INSERT INTO tablet (modelNumber, quantity, name, weight, weightFormat, price, priceFormat, brandName,
                                        type, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat,
                                        os, batteryInfo, dx, dy, dz, dimensionFormat, cameraInfo, size, sizeFormat)
                    VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price}, '{priceFormat}',
                                        '{brandName}', '{type}', {ramSize}, '{ramFormat}', '{processorType}', {numCores},
                                        {hardDriveSize}, '{hardDriveFormat}', '{os}', '{batteryInfo}', {dx}, {dy}, {dz},
                                        '{dimensionFormat}', '{cameraInfo}', {size}, '{sizeFormat}');
                """.format(**tablet)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

            for tabletID in tabletIDs:
                query = """
                    INSERT INTO tabletID (serialNum, modelNum, isLocked)
                    VALUES ('{serialNum}', '{modelNum}', {isLocked});
                """.format(**tabletID)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)
