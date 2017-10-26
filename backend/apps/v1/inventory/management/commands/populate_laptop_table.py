from django.core.management.base import BaseCommand
from backend.utils.database import Database


laptops = [
    dict(
        modelNumber='XPXPXPXPXPXP',
        quantity=987,
        name='XPS',
        weight=15.0,
        weightFormat='lbs',
        price=1299.99,
        priceFormat='CAD',
        brandName='DELL',
        type='laptop',
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
        modelNumber='QWERTERTERRK',
        quantity=23,
        name='Test',
        weight=25.0,
        weightFormat='lbs',
        price=3299.99,
        priceFormat='CAD',
        brandName='Apple',
        type='laptop',
        ramSize=16,
        ramFormat='GB',
        processorType='INTEL',
        numCores=16,
        hardDriveSize=3,
        hardDriveFormat='TB',
        containsCamera=1,
        isTouch=0,
        batteryInfo='10000mAH',
        os='iOS',
        size=17,
        sizeFormat='in'
    )
]

laptopIDs = [
	dict(
	    serialNum='f569s79874',
	    modelNum='XPXPXPXPXPXP',
	    isLocked=0
	),
	dict(
	    serialNum='QWERTERTERRK',
	    modelNum='PPPPPP',
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
