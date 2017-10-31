from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create laptop table'

    def handle(self, *args, **options):

        with Database() as cursor:
            query = """
                CREATE TABLE laptop (
                    modelNumber varchar(255) NOT NULL,
                    quantity integer(11) NOT NULL,
                    name varchar(255) NOT NULL,
                    weight double NOT NULL,
                    weightFormat varchar(255) NOT NULL,
                    price double NOT NULL,
                    priceFormat varchar(255) NOT NULL,
                    brandName varchar(255) NOT NULL,
                    type varchar(255) NOT NULL,
                    ramSize integer(11) NOT NULL,
                    ramFormat varchar(255) NOT NULL,
                    processorType varchar(255) NOT NULL,
                    numCores integer(11) NOT NULL,
                    hardDriveSize double NOT NULL,
                    hardDriveFormat integer(11) NOT NULL,
                    containsCamera tinyint(1) NOT NULL,
                    isTouch tinyint(1) NOT NULL,
                    batteryInfo varchar(255) NOT NULL,
                    os varchar(255) NOT NULL,
                    size double NOT NULL,
                    sizeFormat varchar(255) NOT NULL,
                    PRIMARY KEY (modelNumber)
                );
            """
            
            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
             
            query = """
                CREATE TABLE laptopID (
                    serialNum varchar(255) NOT NULL,
                    modelNum varchar(255) NOT NULL,
                    isLocked tinyint(1) DEFAULT 0,
                    PRIMARY KEY (serialNum),
                    FOREIGN KEY (modelNum) REFERENCES laptop (modelNumber)
                );
            """
            
            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
