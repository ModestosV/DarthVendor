from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sqlite3 import dbapi2 as Database


class Command(BaseCommand):
    help = 'Create tablet table'

    def handle(self, *args, **options):

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        cursor = connection.cursor()
        query = """
            CREATE TABLE tablet (
                modelNumber string NOT NULL,
                ramSize integer NOT NULL,
                ramFormat string NOT NULL,
                processorType string NOT NULL,
                numCores integer NOT NULL,
                hardDriveSize double NOT NULL,
                hardDriveFormat string NOT NULL,
                os string NOT NULL,
                batteryInfo string NOT NULL,
                dx double NOT NULL,
                dy double NOT NULL,
                dz double NOT NULL,
                dimensionFormat string NOT NULL,
                cameraInfo string NOT NULL,
                size double NOT NULL,
                sizeFormat string NOT NULL,
                PRIMARY KEY (modelNumber),
                FOREIGN KEY (modelNumber) REFERENCES item (modelNumber)
            );
        """

        try:
            cursor.execute(query)
        except Exception as error: 
            print(error)  

        connection.commit()
        connection.close()
