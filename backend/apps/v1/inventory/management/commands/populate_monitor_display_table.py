from django.core.management.base import BaseCommand
from backend.utils.database import Database


monitors = [
    dict(
        modelNumber='VE208T',
        name='Widescreen LED Monitor',
        quantity=5,
        weight=11.4,
        weightFormat='kg',
        price=139.99,
        priceFormat='CAD',
        brandName='ASUS',
        type='monitor',
        size=20,
        sizeFormat='inch'
    ),
    dict(
        modelNumber='VP239H',
        name='Wall Mountable IPS Frame-less Monitor',
        quantity=5,
        weight=12.6,
        weightFormat='lbs',
        price=189.99,
        priceFormat='CAD',
        brandName='ASUS',
        type='monitor',
        size=23,
        sizeFormat='inch'
    ),
    dict(
        modelNumber='34UM58',
        name='IPS Widescreen LED Monitor',
        quantity=5,
        weight=13.5,
        weightFormat='lbs',
        price=429.00,
        priceFormat='CAD',
        brandName='LG',
        type='monitor',
        size=25,
        sizeFormat='inch'
    ),
    dict(
        modelNumber='U2415',
        name='Ultrasharp LED Monitor',
        quantity=5,
        weight=18,
        weightFormat='lbs',
        price=419.99,
        priceFormat='CAD',
        brandName='Dell',
        type='monitor',
        size=24,
        sizeFormat='inch'
    ),
    dict(
        modelNumber='MB168B',
        name='Portable USB-powered monitor',
        quantity=5,
        weight=10.6,
        weightFormat='lbs',
        price=199.00,
        priceFormat='CAD',
        brandName='Dell',
        type='monitor',
        size=13,
        sizeFormat='inch'
    ),
    dict(
        modelNumber='23MP48HQ',
        name='IPS Widescreen LED Monitor',
        quantity=5,
        weight=11.5,
        weightFormat='lbs',
        price=159.99,
        priceFormat='CAD',
        brandName='LG',
        type='monitor',
        size=23,
        sizeFormat='inch'
    ),
    dict(
        modelNumber='Z35P',
        name='Ultra-Wide Curved Monitor',
        quantity=5,
        weight=17.6,
        weightFormat='lbs',
        price=1299.00,
        priceFormat='CAD',
        brandName='Acer',
        type='monitor',
        size=35,
        sizeFormat='inch'
    ),
    dict(
        modelNumber='LH55DMEPLGA',
        name='Direct-Lit LED Digital Signage Display',
        quantity=5,
        weight=33.9,
        weightFormat='lbs',
        price=2399.00,
        priceFormat='CAD',
        brandName='Samsung',
        type='monitor',
        size=55,
        sizeFormat='inch'
    ),
    dict(
        modelNumber='C24F390F',
        name='Curved VA FreeSync Widescreen LED Monitor',
        quantity=5,
        weight=10.3,
        weightFormat='lbs',
        price=279.99,
        priceFormat='CAD',
        brandName='Samsung',
        type='monitor',
        size=23.5,
        sizeFormat='inch'
    ),
    dict(
        modelNumber='E2060SWD',
        name='Curved VA FreeSync Widescreen LED Monitor',
        quantity=5,
        weight=8.3,
        weightFormat='lbs',
        price=109.99,
        priceFormat='CAD',
        brandName='NEC',
        type='monitor',
        size=23.5,
        sizeFormat='inch'
    )
]

monitorDisplayIDs = [
    dict(
        serialNum='11111',
        modelNum='VE208T',
        isLocked=0
    ),
    dict(
        serialNum='22222',
        modelNum='VE208T',
        isLocked=0
    ),
    dict(
        serialNum='33333',
        modelNum='VE208T',
        isLocked=0
    ),
    dict(
        serialNum='44444',
        modelNum='VE208T',
        isLocked=0
    ),
    dict(
        serialNum='55555',
        modelNum='VE208T',
        isLocked=0
    ),
    dict(
        serialNum='66666',
        modelNum='VE208T',
        isLocked=0
    ),
    dict(
        serialNum='77777',
        modelNum='VE208T',
        isLocked=0
    ),
    dict(
        serialNum='88888',
        modelNum='VE208T',
        isLocked=0
    ),
    dict(
        serialNum='99999',
        modelNum='VE208T',
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
