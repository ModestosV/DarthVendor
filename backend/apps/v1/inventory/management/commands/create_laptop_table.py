from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create laptop table'

    def handle(self, *args, **options):

        with Database() as cursor:
            query = """
                CREATE TABLE laptop (
                    modelNumber varchar(255) NOT NULL,
                    ramSize integer NOT NULL,
                    ramFormat varchar(255) NOT NULL,
                    processorType varchar(255) NOT NULL,
                    numCores integer NOT NULL,
                    hardDriveSize double NOT NULL,
                    hardDriveFormat integer NOT NULL,
                    containsCamera integer NOT NULL,
                    isTouch integer NOT NULL,
                    batteryInfo varchar(255) NOT NULL,
                    os varchar(255) NOT NULL,
                    size double NOT NULL,
                    sizeFormat varchar(255) NOT NULL,
                    PRIMARY KEY (modelNumber),
                    FOREIGN KEY (modelNumber) REFERENCES item(modelNumber)
                );
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
