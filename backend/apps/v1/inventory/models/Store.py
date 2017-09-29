from django.conf import settings
from sqlite3 import dbapi2 as Database
from backend.apps.v1.inventory.models.Inventory import Inventory


class Store(object):
    """Constructor"""

    def __init__(self):
        self.inventory = Inventory()

    def confirmItemCreation(self, item):
        self.inventory.addItem(item)

    def requestInventoryList(self):
        return self.inventory.requestInventoryList()
