

class ItemAdminUOW:

    def __init__(self):
        self.lockedItemSpecTDGs = list()
        self.lockedItemIDTDGs = list()
        self.dirtySpecs = list()
        self.newSpecs = list()
        self.newItemIDs = list()
        self.deleteItemIDs = list()

    def registerNewSpec(self, spec)
