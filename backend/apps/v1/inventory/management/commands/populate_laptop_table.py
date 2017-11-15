from django.core.management.base import BaseCommand
from backend.utils.database import Database


laptops = [
    dict(
        modelNumber='80TV00W1US',
        quantity=5,
        name='IdeaPad 310',
        weight=4.84,
        weightFormat='lbs',
        price=679.88,
        priceFormat='CAD',
        brandName='Lenovo',
        type='laptop',
        ramSize=4,
        ramFormat='GB',
        processorType='Intel i7-7500',
        numCores=2,
        hardDriveSize=1,
        hardDriveFormat='TB',
        containsCamera=0,
        isTouch=0,
        batteryInfo='2-Cell Lithium Polymer',
        os='Windows 10 Home',
        size=15.6,
        sizeFormat='in'
    ),
    dict(
        modelNumber='GT73VR',
        quantity=5,
        name='Titan Gaming Notebook',
        weight=8.6,
        weightFormat='lbs',
        price=2349.88,
        priceFormat='CAD',
        brandName='MSI',
        type='laptop',
        ramSize=32,
        ramFormat='GB',
        processorType='ntel i7-7700HQ',
        numCores=4,
        hardDriveSize=2,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=0,
        batteryInfo='8 cell 5225mAH',
        os='Windows 10 Professional',
        size=17.3,
        sizeFormat='in'
    ),
    dict(
        modelNumber='A1706',
        quantity=5,
        name='MacBook Pro',
        weight=4.02,
        weightFormat='lbs',
        price=1599.00,
        priceFormat='CAD',
        brandName='Apple',
        type='laptop',
        ramSize=16,
        ramFormat='GB',
        processorType='Intel Core i7',
        numCores=4,
        hardDriveSize=2,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=0,
        batteryInfo='76 WHr Lithium-Polymer',
        os='Mac OS X v10.12 Sierra',
        size=15.4,
        sizeFormat='in'
    ),
    dict(
        modelNumber='MQD32LL',
        quantity=5,
        name='MacBook Air Notebook',
        weight=2.96,
        weightFormat='lbs',
        price=1169.00,
        priceFormat='CAD',
        brandName='Apple',
        type='laptop',
        ramSize=8,
        ramFormat='GB',
        processorType='Intel Core i5-5350U',
        numCores=2,
        hardDriveSize=0.5,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=0,
        batteryInfo='54 WHr Lithium-Polymer',
        os='Mac OS X v10.12 Sierra',
        size=13.3,
        sizeFormat='in'
    ),
    dict(
        modelNumber='YOGA 910',
        quantity=5,
        name='YOGA 910 Ultrabook',
        weight=3.04,
        weightFormat='lbs',
        price=1879.00,
        priceFormat='CAD',
        brandName='Lenovo',
        type='laptop',
        ramSize=8,
        ramFormat='GB',
        processorType='Intel Core i7-7500U',
        numCores=2,
        hardDriveSize=3,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=0,
        batteryInfo='4-cell 78Wh',
        os='Windows 10 Home',
        size=13.3,
        sizeFormat='in'
    ),
    dict(
        modelNumber='UX501VW',
        quantity=5,
        name='ZenBook Pro Ultrabook',
        weight=5.1,
        weightFormat='lbs',
        price=1749.88,
        priceFormat='CAD',
        brandName='Asus',
        type='laptop',
        ramSize=16,
        ramFormat='GB',
        processorType='Intel Core I7-6700HQ',
        numCores=2,
        hardDriveSize=1,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=0,
        batteryInfo='4-cell 78Wh',
        os='Windows 10 Professional',
        size=15.6,
        sizeFormat='in'
    ),
    dict(
        modelNumber='R541UA',
        quantity=5,
        name='RB51 Notebook ',
        weight=4.4,
        weightFormat='lbs',
        price=599.88,
        priceFormat='CAD',
        brandName='Asus',
        type='laptop',
        ramSize=8,
        ramFormat='GB',
        processorType='Intel i5-6198DU',
        numCores=1,
        hardDriveSize=1,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=0,
        batteryInfo='3-cell Li-ion',
        os='Windows 10 Enterprise',
        size=15.6,
        sizeFormat='in'
    ),
    dict(
        modelNumber='F240CA',
        quantity=5,
        name='F24 Notebook',
        weight=4.80,
        weightFormat='lbs',
        price=549.00,
        priceFormat='CAD',
        brandName='HP',
        type='laptop',
        ramSize=4,
        ramFormat='GB',
        processorType='AMD E1-2100',
        numCores=1,
        hardDriveSize=0.5,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=0,
        batteryInfo='3-cell 31WHr',
        os='Windows 8.1',
        size=15.6,
        sizeFormat='in'
    ),
    dict(
        modelNumber='k250ca',
        quantity=5,
        name='Canada Bilingual Gaming Notebook ',
        weight=6.33,
        weightFormat='lbs',
        price=1399.00,
        priceFormat='CAD',
        brandName='HP',
        type='laptop',
        ramSize=8,
        ramFormat='GB',
        processorType='Intel Core i7-5500U',
        numCores=2,
        hardDriveSize=1,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=0,
        batteryInfo='4 Cell 41WHr',
        os='Windows 8.1',
        size=17.3,
        sizeFormat='in'
    ),
    dict(
        modelNumber='5328BLK',
        quantity=5,
        name='Dell Inspiron 15',
        weight=5.67,
        weightFormat='lbs',
        price=999.00,
        priceFormat='CAD',
        brandName='HP',
        type='laptop',
        ramSize=8,
        ramFormat='GB',
        processorType='Intel Core i5-7300',
        numCores=2,
        hardDriveSize=1,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=0,
        batteryInfo='6-Cell 74WHr',
        os='Windows 10 Home',
        size=15.6,
        sizeFormat='in'
    )
]

laptopIDs = [
    dict(
        serialNum='f569s79874',
        modelNum='GT73VR',
        isLocked=0
    ),
    dict(
        serialNum='QWERTERTERRK',
        modelNum='GT73VR',
        isLocked=0
    )
]


class Command(BaseCommand):
    help = 'Populate laptop table'

    def handle(self, *args, **options):

        with Database() as cursor:

            for laptop in laptops:
                query = """
                    INSERT INTO laptop (modelNumber, quantity, name, weight, weightFormat, price,
                    priceFormat, brandName, type, ramSize, ramFormat, processorType, numCores,
                    hardDriveSize, hardDriveFormat, containsCamera, isTouch, batteryInfo, os,
                           size, sizeFormat)
                    VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price},
                            '{priceFormat}', '{brandName}', '{type}', {ramSize}, '{ramFormat}',
                            '{processorType}', {numCores}, {hardDriveSize}, '{hardDriveFormat}',
                             {containsCamera}, {isTouch}, '{batteryInfo}', '{os}',
                             {size}, '{sizeFormat}');
                """.format(**laptop)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

            for laptopID in laptopIDs:
                query = """
                    INSERT INTO laptopID (serialNum, modelNum, isLocked)
                    VALUES ('{serialNum}', '{modelNum}', {isLocked});
                """.format(**laptopID)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)
