from django.conf import settings
from sqlite3 import dbapi2


def dict_factory(cursor, row):
    """
        Helper function to convert the cursor results from tuple to dictionary.

        Source: https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory
    """

    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Database:
    """ SQLite database class.

    Attributes:
        path (str): Location of the *.sqlite file.
        connection: Connection.
        cursor: Cursor.
    """

    def __init__(self, path=None):
        """ Construct Database object.
            
            Args:
                path (str): Location of the *.sqlite file. 
        """
        
        if path: 
            self.path = path
        else:
            self.path = settings.DATABASES['default']['NAME']

        self.connection = dbapi2.connect(settings.DATABASES['default']['NAME'])
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def __enter__(self):
        """ Returns cursor. """
        return self.cursor

    def __exit__(self, type, value, traceback):
        """ Close connection on exit. """
        self.connection.commit()
        self.connection.close()