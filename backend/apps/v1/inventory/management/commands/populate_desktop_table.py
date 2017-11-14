from django.core.management.base import BaseCommand
from backend.utils.database import Database


desktops = [
    dict(
        modelNumber='VR7RC',
        quantity=5,
        name='Trident 3',
        weight=21,
        weightFormat='lbs',
        price=1449.00,
        priceFormat='CAD',
        brandName='MSI',
        type='desktop',
        ramSize=8,
        ramFormat='GB',
        processorType='Core i7-7700',
        numCores=4,
        hardDriveSize=1,
        hardDriveFormat='TB',
        dx=13,
        dy=21,
        dz=20,
        dimensionFormat='INCH'
    ),
    dict(
        modelNumber='VR8RE',
        quantity=5,
        name='MSI Infinite X',
        weight=25.0,
        weightFormat='lbs',
        price=2799.00,
        priceFormat='CAD',
        brandName='MSI',
        type='desktop',
        ramSize=16,
        ramFormat='GB',
        processorType='i7-8700k',
        numCores=4,
        hardDriveSize=2,
        hardDriveFormat='TB',
        dx=14,
        dy=22,
        dz=24,
        dimensionFormat='INCH'
    ),
    dict(
        modelNumber='CS9000009',
        quantity=5,
        name='CORSAIR ONE PRO TI',
        weight=30.0,
        weightFormat='lbs',
        price=3449.99,
        priceFormat='CAD',
        brandName='Corsair',
        type='desktop',
        ramSize=32,
        ramFormat='GB',
        processorType='Intel i7-7700K',
        numCores=4,
        hardDriveSize=1,
        hardDriveFormat='TB',
        dx=12,
        dy=23,
        dz=21,
        dimensionFormat='INCH'
    ),
    dict(
        modelNumber='DS71',
        quantity=5,
        name='ASUS G11CD',
        weight=33.0,
        weightFormat='lbs',
        price=1349.00 ,
        priceFormat='CAD',
        brandName='ASUS',
        type='desktop',
        ramSize=8,
        ramFormat='GB',
        processorType='Intel Core i7-7700K',
        numCores=4,
        hardDriveSize=1,
        hardDriveFormat='TB',
        dx=11.5,
        dy=22,
        dz=24.5,
        dimensionFormat='INCH'
    ),
    dict(
        modelNumber='US010T',
        quantity=5,
        name='ASUS M32CD',
        weight=22.0,
        weightFormat='lbs',
        price=1179.00,
        priceFormat='CAD',
        brandName='ASUS',
        type='desktop',
        ramSize=8,
        ramFormat='GB',
        processorType='Intel Core i7-6700K',
        numCores=4,
        hardDriveSize=2,
        hardDriveFormat='TB',
        dx=10.5,
        dy=20,
        dz=23,
        dimensionFormat='INCH'
    ),
    dict(
        modelNumber='5168BLK',
        quantity=5,
        name='Dell Inspiron',
        weight=19.0,
        weightFormat='lbs',
        price=649.00,
        priceFormat='CAD',
        brandName='Dell',
        type='desktop',
        ramSize=4,
        ramFormat='GB',
        processorType='Intel Core i5-7400K',
        numCores=2,
        hardDriveSize=1,
        hardDriveFormat='TB',
        dx=9,
        dy=18,
        dz=20.5,
        dimensionFormat='INCH'
    ),
    dict(
        modelNumber='7512SLV',
        quantity=5,
        name='Dell Alienware Gaming Desktop',
        weight=19.0,
        weightFormat='lbs',
        price=1999.00,
        priceFormat='CAD',
        brandName='Dell',
        type='desktop',
        ramSize=16,
        ramFormat='GB',
        processorType='Intel Core i7-7700K',
        numCores=4,
        hardDriveSize=1.5,
        hardDriveFormat='TB',
        dx=12.5,
        dy=19,
        dz=22,
        dimensionFormat='INCH'
    ),
    dict(
        modelNumber='GBBXi5',
        quantity=5,
        name='BRIX Barebone System',
        weight=1.69,
        weightFormat='lbs',
        price=499.88,
        priceFormat='CAD',
        brandName='Gigabyte',
        type='desktop',
        ramSize=4,
        ramFormat='GB',
        processorType='Intel Core i5-4570',
        numCores=4,
        hardDriveSize=0.5,
        hardDriveFormat='TB',
        dx=4.5,
        dy=4.4,
        dz=2.4,
        dimensionFormat='INCH'
    ),
    dict(
        modelNumber='GBBACE3',
        quantity=5,
        name='Barebone Mini Desktop',
        weight=1.44,
        weightFormat='lbs',
        price=179.99,
        priceFormat='CAD',
        brandName='Gigabyte',
        type='desktop',
        ramSize=1,
        ramFormat='GB',
        processorType='Intel Celeron N3000',
        numCores=1,
        hardDriveSize=0.5,
        hardDriveFormat='TB',
        dx=2.2,
        dy=4.2,
        dz=4.5,
        dimensionFormat='INCH'
    )

]

desktopIDs = [
    dict(
        serialNum='4569s79874',
        modelNum='ZZZZZZZ',
        isLocked=0
    ),
    dict(
        serialNum='45698756x4',
        modelNum='PPPPPP',
        isLocked=0
    )
]


class Command(BaseCommand):
    help = 'Populate desktop table'

    def handle(self, *args, **options):

        with Database() as cursor:

            for desktop in desktops:
                query = """
                    INSERT INTO desktop (modelNumber, quantity, name, weight, weightFormat, price,
                        priceFormat, brandName, type, ramSize, ramFormat, processorType, numCores, hardDriveSize,
                        hardDriveFormat, dx, dy, dz, dimensionFormat)
                    VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price},
                        '{priceFormat}', '{brandName}', '{type}', {ramSize}, '{ramFormat}', '{processorType}', {numCores}, {hardDriveSize},
                        '{hardDriveFormat}', {dx}, {dy}, {dz}, '{dimensionFormat}');
                """.format(**desktop)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

            for desktopID in desktopIDs:
                query = """
                INSERT INTO desktopID (serialNum, modelNum, isLocked)
                VALUES ('{serialNum}', '{modelNum}', {isLocked});
            """.format(**desktopID)

                try:
                    cursor.execute(query)
                except Exception as error:
                        print(error)
