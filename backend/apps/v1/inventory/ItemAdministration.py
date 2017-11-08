from backend.apps.v1.inventory.ItemAdminUOW import ItemAdminUOW
from backend.apps.v1.inventory.models.ItemID import ItemID

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
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
        for i in range(0, quantity):
            serialNumber = uuid.uuid1().hex
            itemID = ItemID(serialNumber, False, spec)
            self.uow.registerNewItemID(itemID)
        return

    def viewInventory(self):
        types = ["DESKTOP", "MONITOR", "TABLET", "LAPTOP"]

        result = []
        for specType in types:
            result += ItemSpecMapper.findAll({'type': specType})

        print(result)
        return
