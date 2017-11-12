from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper


class Catalog:

    @staticmethod
    def getAllSpecs():
        types = ["MONITOR", "DESKTOP", "TABLET", "LAPTOP"]
        specs = list()
        for specType in types:
            specs += ItemSpecMapper.findAll({'type': specType})
        return specs
