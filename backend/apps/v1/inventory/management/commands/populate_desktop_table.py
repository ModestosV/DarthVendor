from django.core.management.base import BaseCommand
from backend.utils.database import Database


desktops = [
    dict(
        modelNumber='ZZZZZZZ',
        quantity=46,
        name='Razer Desktop',
        weight=15.0,
        weightFormat='lbs',
        price=2299.99,
        priceFormat='CAD',
        brandName='RAZER', 
        ramSize=16,
        ramFormat='GB',
        processorType='INTEL',
        numCores=4,
        hardDriveSize=2,
        hardDriveFormat='TB',
        dx=15,
        dy=30,
        dz=1,
        dimensionFormat='INCH'
    ),
    dict(
        modelNumber='PPPPPP',
        quantity=5,
        name='Apple Desktop',
        weight=12.0,
        weightFormat='lbs',
        price=3299.99,
        priceFormat='CAD',
        brandName='APPLE', 
        ramSize=16,
        ramFormat='GB',
        processorType='INTEL',
        numCores=4,
        hardDriveSize=1,
        hardDriveFormat='TB',
        dx=12,
        dy=33,
        dz=1,
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
                        priceFormat, brandName, ramSize, ramFormat, processorType, numCores, hardDriveSize,
                        hardDriveFormat, dx, dy, dz, dimensionFormat)
                    VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price},
                        '{priceFormat}', '{brandName}', {ramSize}, '{ramFormat}', '{processorType}', {numCores}, {hardDriveSize},
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
		
