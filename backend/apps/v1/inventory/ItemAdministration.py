from backend.apps.v1.inventory.models.Catalog import Catalog

from backend.apps.v1.inventory.ItemAdminUOW import ItemAdminUOW
from backend.apps.v1.inventory.models.ItemID import ItemID

from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper

import uuid
from contracts import contract


class ItemAdministration:

    def __init__(self):
        self.uow = None

    @contract(returns='bool|None')
    def initiateEdit(self):
        self.uow = ItemAdminUOW()
        return True

    @contract(returns='bool|None')
    def terminateEdit(self):
        self.uow.commit()
        self.uow = None
        return True

    @contract(returns='bool|None')
    def cancelEdit(self):
        self.uow = None
        return True

    @contract(returns='bool|None')
    def addItemSpec(self, itemSpec):
        self.uow.registerNewSpec(itemSpec)
        return True

    @contract(returns='bool|None')
    def modifyItemSpec(self, itemSpec):
        self.uow.registerDirtySpec(itemSpec)
        return True

    @contract(returns='bool|None')
    def deleteItem(self, itemID):
        self.uow.registerDeletedItemID(itemID)
        return True

    def deleteSpec(self, itemSpec):
        self.uow.registerDeletedSpec(itemSpec)
        return True
        
    @contract(modelNumber='str', specType='str', quantity='int,>0', returns='bool|None')
    def addQuantity(self, modelNumber, specType, quantity):
        spec = ItemSpecMapper.find(modelNumber, specType)
        for i in range(0, int(quantity)):
            serialNumber = uuid.uuid4().hex
            itemID = ItemID(serialNumber, False, spec)
            self.uow.registerNewItemID(itemID)
        return True

    @contract(returns='list|None')
    def getCatalog(self):
        return Catalog.getAllSpecs()

    @contract(modelNumber='str', specType='str')
    def getItemIDs(self, modelNumber, specType):
        spec = ItemSpecMapper.find(modelNumber, specType)
        return ItemIDMapper.find(spec)
