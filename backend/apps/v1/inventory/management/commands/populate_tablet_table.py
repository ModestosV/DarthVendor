from django.core.management.base import BaseCommand
from backend.utils.database import Database


tablets = [
    dict(
        modelNumber='ME176C',
        quantity=5,
        name='ASUS ZenPad Tablet',
        weight=0.58,
        weightFormat='lbs',
        price=154.00 ,
        priceFormat='CAD',
        brandName='ASUS',
        type='tablet',
        ramSize=1,
        ramFormat='GB',
        processorType='Intel Atom',
        numCores=4,
        hardDriveSize=16,
        hardDriveFormat='GB',
        os='Android',
        batteryInfo='13Wh Li-polymer Battery',
        dx=189,
        dy=108,
        dz=0.84,
        dimensionFormat='CM',
        cameraInfo='Camera Rear',
        size=2.0,
        sizeFormat='PX'
    ),
    dict(
        modelNumber='MGTX2CL',
        quantity=5,
        name='iPad Air 2',
        weight=1.75,
        weightFormat='lbs',
        price=749.99,
        priceFormat='CAD',
        brandName='Apple',
        type='tablet',
        ramSize=2,
        ramFormat='GB',
        processorType='Apple A8X',
        numCores=3,
        hardDriveSize=128,
        hardDriveFormat='GB',
        os='iOS 8.1',
        batteryInfo='Li-Po 7340 mAh',
        dx=24,
        dy=16.9,
        dz=0.6,
        dimensionFormat='CM',
        cameraInfo='Camera Rear',
        size=8.0,
        sizeFormat='PX'
    ),
    dict(
        modelNumber='A1489',
        quantity=5,
        name='iPad mini 2 Wi-Fi',
        weight=0.72,
        weightFormat='lbs',
        price=224.99,
        priceFormat='CAD',
        brandName='Apple',
        type='tablet',
        ramSize=1,
        ramFormat='GB',
        processorType='1.3 GHz Cyclone',
        numCores=2,
        hardDriveSize=64,
        hardDriveFormat='GB',
        os='iOS 7',
        batteryInfo='Li-Po 6470 mAh',
        dx=240,
        dy=13.4,
        dz=0.7,
        dimensionFormat='CM',
        cameraInfo='Camera Front',
        size=5.0,
        sizeFormat='PX'
    ),
    dict(
        modelNumber='T560NZWUXAC',
        quantity=5,
        name='Galaxy Tab E 9.6',
        weight=1.2,
        weightFormat='lbs',
        price=329.99,
        priceFormat='CAD',
        brandName='Samsung',
        type='tablet',
        ramSize=1.5,
        ramFormat='GB',
        processorType='Quad-Core',
        numCores=4,
        hardDriveSize=32,
        hardDriveFormat='GB',
        os='Android 5.0',
        batteryInfo='4000 mAh',
        dx=24.1,
        dy=14.9,
        dz=0.9,
        dimensionFormat='CM',
        cameraInfo='Camera Front',
        size=2.0,
        sizeFormat='PX'
    ),
    dict(
        modelNumber='B1-780-K6C3',
        quantity=5,
        name='ICONIA MediaTek',
        weight=0.55,
        weightFormat='lbs',
        price=109.99,
        priceFormat='CAD',
        brandName='Acer',
        type='tablet',
        ramSize=1,
        ramFormat='GB',
        processorType='1.30 GHz Quad-core',
        numCores=4,
        hardDriveSize=24,
        hardDriveFormat='GB',
        os='Android 4.0',
        batteryInfo=' Li-Polymer 2780 mAh',
        dx=19,
        dy=10.16,
        dz=1.0,
        dimensionFormat='CM',
        cameraInfo='Camera Rear',
        size=2.0,
        sizeFormat='PX'
    )
]

tabletIDs = [
    dict(
        serialNum='f569g79874',
        modelNum='ME176C',
        isLocked=0
    ),
    dict(
        serialNum='bWERTERTERRK',
        modelNum='ME176C',
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
