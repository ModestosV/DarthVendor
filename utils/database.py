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
