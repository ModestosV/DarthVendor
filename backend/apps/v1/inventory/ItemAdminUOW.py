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

        # attempt to lock appropriate table if necessary
        if spec.type not in self.lockedSpecTDGs:
            lockStatus = ItemSpecMapper.lock(spec.type, self)

            if lockStatus:
                self.lockedSpecTDGs.append(spec.type)
            else:
                return False

        # if the table is available the operation can proceed
        if spec.type in self.lockedSpecTDGs:
            # check if an spec with this modelnumber was already added to the UOW
            for newSpec in self.newSpecs:
                if spec.modelNumber == newSpec.modelNumber:
                    return False

            for dirtySpec in self.dirtySpecs:
                if spec.modelNumber == dirtySpec.modelNumber:
                    return False

            # check if a spec with this modelnumber exists in the database, if not add to newSpecs
            existingSpec = ItemSpecMapper.find(spec.modelNumber, spec.type)

            if existingSpec is not None:
                return False
            else:
                self.newSpecs.append(spec)
                return True

    def registerDirtySpec(self, spec):
        if spec.type not in self.lockedSpecTDGs:
            lockStatus = ItemSpecMapper.lock(spec.type, self)

            if lockStatus:
                self.lockedSpecTDGs.append(spec.type)
            else:
                return False

        if spec.type in self.lockedSpecTDGs:
            # if a spec with this modelnumber was already added to the UOW as a new spec, if so, replace it with the new version
            for newSpec in self.newSpecs:
                if spec.modelNumber == newSpec.modelNumber:
                    self.newSpecs.remove(newSpec)
                    self.newSpecs.append(spec)
                    return True

            # if a spec with this modelnumber was already added as dirty, replace it with the new one
            for dirtySpec in self.dirtySpecs:
                if spec.modelNumber == dirtySpec.modelNumber:
                    self.dirtySpecs.remove(dirtySpec)
                    self.dirtySpecs.append(spec)
                    return True

            # if it wasnt added to dirty or new specs, add it to dirty
            self.dirtySpecs.append(spec)
            return True

    def registerNewItemID(self, itemID):
        if itemID.spec.type not in self.lockedItemIDTDGs:
            lockStatus = ItemIDMapper.lock(itemID.spec.type)

            if lockStatus:
                self.lockedItemIDTDGs.append(itemID.spec.type)
            else:
                return False

        if itemID.spec.type in self.lockedItemIDTDGs:
            self.newItemIDs.append(itemID)
            return True

    def registerDeletedItemID(self, itemID):
        if itemID.spec.type not in self.lockedItemIDTDGs:
            lockStatus = ItemIDMapper.lock(itemID.spec.type)

            if lockStatus:
                self.lockedItemIDTDGs.append(itemID.spec.type)
            else:
                return False

        if itemID.spec.type in self.lockedItemIDTDGs:
            self.deletedItemIDs.append(itemID)
            return True

    def commit(self):

        for spec in self.newSpecs:
            ItemSpecMapper.insert(spec)

        for spec in self.dirtySpecs:
            ItemSpecMapper.update(spec)

        for tdgType in self.lockedSpecTDGs:
            ItemSpecMapper.unlock(tdgType, self)

        selflockedSpecTDGs = []

        for itemID in self.newItemIDs:
            ItemIDMapper.insert(itemID)

        for itemID in self.deletedItemIDs:
            ItemIDMapper.delete(itemID)

        for tdgType in self.lockedItemIDTDGs:
            ItemIDMapper.unlock(tdgType, self)

        self.lockedItemIDTDGs = []

        return
