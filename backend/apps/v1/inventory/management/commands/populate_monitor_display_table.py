from django.core.management.base import BaseCommand
from backend.utils.database import Database


monitors = [
    dict(
        modelNumber='x123131',
        name='Gaming Monitor',
        quantity=5,
        weight=10.0,
        weightFormat='lbs',
        price=9.99,
        priceFormat='CAD',
        brandName='SONY',
        type='monitor',
        size=30.5,
        sizeFormat='inch'
    ),
    dict(
        modelNumber='v123131',
        name='Regular Monitor',
        quantity=5,
        weight=10.0,
        weightFormat='lbs',
        price=9.99,
        priceFormat='CAD',
        brandName='SORNY',
        type='monitor',
        size=30.5,
        sizeFormat='inch'
    )
]

monitorDisplayIDs = [
	dict(
	    serialNum='g569s79874',
	    modelNum='x123131',
	    isLocked=0
	),
	dict(
	    serialNum='TWERTERTERRK',
	    modelNum='v123131',
	    isLocked=0
	)
]

class Command(BaseCommand):
    help = 'Populate monitor display table'

    def handle(self, *args, **options):

        with Database() as cursor:

            for monitor in monitors:
                query = """
                    INSERT INTO monitorDisplay (modelNumber, quantity, name, weight, weightFormat, price, priceFormat, 
                                                brandName, type, size, sizeFormat)
                    VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price}, '{priceFormat}', 
                             '{brandName}', '{type}', {size}, '{sizeFormat}');
                """.format(**monitor)

                try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)
                    
            for monitorDisplayID in monitorDisplayIDs:
                 query = """
		            INSERT INTO monitorDisplayID (serialNum, modelNum, isLocked)
		            VALUES ('{serialNum}', '{modelNum}', {isLocked});
		         """.format(**monitorDisplayID)
				
	             try:
                    cursor.execute(query)
                except Exception as error:
                    print(error)                    
