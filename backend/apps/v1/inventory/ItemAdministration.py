from backend.apps.v1.inventory.models.Catalog import Catalog

from backend.apps.v1.inventory.ItemAdminUOW import ItemAdminUOW
from backend.apps.v1.inventory.models.ItemID import ItemID

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper

import uuid


class ItemAdministration:

    def __init__(self):
        self.uow = None

    def initiateEdit(self):
        self.uow = ItemAdminUOW()
        return

    def terminateEdit(self):
        self.uow.commit()
        self.uow = None
        return

    def addItemSpec(self, itemSpec):
        self.uow.registerNewSpec(itemSpec)
        return

    def modifyItemSpec(self, itemSpec):
        self.uow.registerDirtySpec(itemSpec)
        return

    def deleteItem(self, itemID):
        self.uow.registerDeletedItemID(itemID)
        return

    def addQuantity(self, modelNumber, specType, quantity):
        spec = ItemSpecMapper.find(modelNumber, specType)
        for i in range(0, int(quantity)):
            serialNumber = uuid.uuid4().hex
            itemID = ItemID(serialNumber, False, spec)
            self.uow.registerNewItemID(itemID)
        return True

    def getCatalog(self):
        return Catalog.getAllSpecs()

    def getItemIDs(self, modelNumber, specType):
        spec = ItemSpecMapper.find(modelNumber, specType)
        return ItemIDMapper.find(spec)
