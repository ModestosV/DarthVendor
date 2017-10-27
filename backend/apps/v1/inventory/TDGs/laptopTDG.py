from backend.utils.database import Database


class TabletTDG:
    owner = None

    @staticmethod
    def insert(laptop):

        with Database() as cursor:
            query = """
                INSERT INTO laptop (modelNumber, quantity, name, weight, weightFormat, price, priceFormat, brandName,
                                    type, ramSize, ramFormat, processorType, numCores, hardDriveSize, hardDriveFormat,
                                    os, batteryInfo, dx, dy, dz, dimensionFormat, cameraInfo, size, sizeFormat)
                VALUES ('{modelNumber}', {quantity}, '{name}', {weight}, '{weightFormat}', {price}, '{priceFormat}',
                                    '{brandName}', '{type}', {ramSize}, '{ramFormat}', '{processorType}', {numCores},
                                    {hardDriveSize}, '{hardDriveFormat}', '{os}', '{batteryInfo}', {dx}, {dy}, {dz},
                                    '{dimensionFormat}', '{cameraInfo}', {size}, '{sizeFormat}');
            """.format(**laptop)

            try:
                cursor.execute(query)
            except Exception as error:
                print(error)
