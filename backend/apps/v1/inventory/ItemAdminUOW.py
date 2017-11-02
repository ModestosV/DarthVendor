from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper



class ItemAdminUOW:

    def __init__(self):
        self.newSpecs = list()
        self.dirtySpecs = list()
        self.newItemIDs = list()
        self.deletedItemIDs = list()

        # list of item type strings for spec TDGs that are locked by this Unit of Work
        self.lockedSpecTDGs = list()

        # list of item type strings for item TDGs that are locked by this Unit of Work
        self.lockedItemIDTDGs = list()

    def registerNewSpec(self, spec):

        if spec.type not in self.lockedSpecTDGs:
            lockStatus = ItemSpecMapper.lock(spec.type, self)

            if lockStatus:
                lockedSpecTDGs.append(spec.type)
            else:
                return False

        if spec.type in self.lockedSpecTDGs:
            # check if an spec with this modelnumber was already added to the UOW
            for newSpec in self.newSpecs:
                if spec.modelnumber == newSpec.modelnumber:
                    return False

            for dirtySpec in self.dirtySpecs:
                if spec.modelnumber == dirtySpec.modelnumber:
                    return False

            existingSpecs = ItemSpecMapper.find(spec)
        return True

    def registerDirtySpec(self, spec):
        return True

    def registerNewItemID(self, itemID):
        return True

    def registerDeletedItemID(self, itemID):
        return True

    def commit():
        return
