from django.core.management.base import BaseCommand
from backend.utils.database import Database


laptops = [
    dict(
        quantity=987,
        weight=15.0,
        weightFormat='lbs',
        price=1299.99,
        priceFormat='CAD',
        brandName='DELL',
        name='XPS',
        type='laptop',
        modelNumber='XPXPXPXPXPXP',
        ramSize=16,
        ramFormat='GB',
        processorType='INTEL',
        numCores=4,
        hardDriveSize=1,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=1,
        batteryInfo='10000mAH',
        os='Windows',
        size=13,
        sizeFormat='PX'
    ),
    dict(
        quantity=671,
        weight=12.0,
        weightFormat='lbs',
        price=1699.99,
        priceFormat='CAD',
        brandName='MICROSOFT',
        name='Surface NoteBook',
        type='laptop',
        modelNumber='SSSSSSSSSS',
        ramSize=16,
        ramFormat='GB',
        processorType='INTEL',
        numCores=4,
        hardDriveSize=2,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=1,
        batteryInfo='13000mAH',
        os='Windows',
        size=14.5,
        sizeFormat='PX'
    )
]


class Command(BaseCommand):
    help = 'Populate laptop table'

    def handle(self, *args, **options):

        with Database() as cursor:

            for laptop in laptops:
                query = """
                    INSERT INTO item (quantity, name, weight, weightFormat, price,
                        priceFormat, brandName, type, modelNumber)
                    VALUES ({quantity}, '{name}', {weight}, '{weightFormat}', 
                        {price}, '{priceFormat}', '{brandName}', '{type}', '{modelNumber}');
                """.format(**laptop)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)

                query = """
                    INSERT INTO laptop (modelNumber, ramSize, ramFormat,
                        processorType, numCores, hardDriveSize, hardDriveFormat,
                        containsCamera, isTouch, batteryInfo, os,
                        size, sizeFormat)
                    VALUES ('{modelNumber}', {ramSize}, '{ramFormat}',
                        '{processorType}', {numCores}, {hardDriveSize}, '{hardDriveFormat}',
                        {containsCamera}, {isTouch}, '{batteryInfo}', '{os}',
                        {size}, '{sizeFormat}');
                """.format(**laptop)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)
