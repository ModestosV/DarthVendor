from django.core.management.base import BaseCommand
from backend.utils.database import Database


class Command(BaseCommand):
    help = 'Create desktop table'

    def handle(self, *args, **options):

        with Database() as cursor:

            query = """
                CREATE TABLE desktop (
                    modelNumber varchar(255) NOT NULL,
                    ramSize integer NOT NULL,
                    ramFormat varchar(255) NOT NULL,
                    processorType varchar(255) NOT NULL,
                    numCores integer NOT NULL,
                    hardDriveSize double NOT NULL,
                    hardDriveFormat varchar(255) NOT NULL,
                    dx double NOT NULL,
                    dy double NOT NULL,
                    dz double NOT NULL,
                    dimensionFormat varchar(255) NOT NULL,
                    PRIMARY KEY (modelNumber),
                    FOREIGN KEY(modelNumber) REFERENCES item(modelNumber)
                );
            """

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
