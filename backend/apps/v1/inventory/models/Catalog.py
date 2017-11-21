from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper
from backend.apps.v1.inventory.mappers.ItemIDMapper import ItemIDMapper


class Catalog:

    @staticmethod
    def getAllSpecs():
        types = ["MONITOR", "DESKTOP", "TABLET", "LAPTOP"]
        specs = list()
        for specType in types:
            specs += ItemSpecMapper.findAll(specType)
        return specs

    def getQuantityOfSpec(modelNumber, type):
        spec = ItemSpecMapper.find(modelNumber, type)
        itemIDs = ItemIDMapper.find(spec)
        return len(itemIDs)
