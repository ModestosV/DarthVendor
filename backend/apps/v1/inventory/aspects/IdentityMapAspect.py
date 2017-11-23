from backend.utils.AOP import intercept


class SpecIdentityMapAspect:

    identityMaps = dict()

    def find_interceptor(original_function, modelNumber, type):
        result = None

        # check if spec is already in identityMap
        if type in SpecIdentityMapAspect.identityMaps:
            if modelNumber in SpecIdentityMapAspect.identityMaps[type]:
                result = SpecIdentityMapAspect.identityMaps[type][modelNumber]

        # if it wasnt already read from the db, run regular find, store result and return it
        if result is None:
            result = original_function(modelNumber, type)

            if type not in SpecIdentityMapAspect.identityMaps:
                SpecIdentityMapAspect.identityMaps[type] = {}

            SpecIdentityMapAspect.identityMaps[type][modelNumber] = result

        return result

    def findAll_interceptor(original_function, type):

        results = original_function(type)

        # insert unsaved results in the identity map, and replace newly loaded instance for previously loaded ones
        for i in range(0, len(results)):
            if type not in SpecIdentityMapAspect.identityMaps:
                SpecIdentityMapAspect.identityMaps[type] = {}

            if modelNumber in SpecIdentityMapAspect.identityMaps[type]:
                results[i] = SpecIdentityMapAspect.identityMaps[type][modelNumber]

            else:
                SpecIdentityMapAspect.identityMaps[type][modelNumber] = results[i]

        return results

    def update_interceptor(original_function, itemSpec):
        # check if spec is already in identityMap

        result = original_function(itemSpec)

        if itemSpec.type not in SpecIdentityMapAspect.identityMaps:
            SpecIdentityMapAspect.identityMaps[itemSpec.type] = {}

        if itemSpec.modelNumber in SpecIdentityMapAspect.identityMaps[itemSpec.type]:
            SpecIdentityMapAspect.identityMaps[itemSpec.type][itemSpec.modelNumber] = None

        return result


class IDIdentityMapAspect:

    identityMaps = dict()

    def findBySerialNumber_interceptor(original_function, serialNumber, itemSpec):
        result = None

        # check if spec is already in identityMap
        if itemSpec.type in IDIdentityMapAspect.identityMaps:
            if modelNumber in IDIdentityMapAspect.identityMaps[itemSpec.type]:
                result = IDIdentityMapAspect.identityMaps[itemSpec.type][serialNumber]

        # if it wasnt already read from the db, run regular find, store result and return it
        if result is None:
            result = original_function(serialNumber, itemSpec)

            if itemSpec.type not in IDIdentityMapAspect.identityMaps:
                IDIdentityMapAspect.identityMaps[itemSpec.type] = {}

            IDIdentityMapAspect.identityMaps[itemSpec.type][serialNumber] = result

        return result

    def find_interceptor(original_function, itemSpec):

        results = original_function(itemSpec)

        # insert unsaved results in the identity map, and replace newly loaded instance for previously loaded ones
        for i in range(0, len(results)):
            if type not in IDIdentityMapAspect.identityMaps:
                IDIdentityMapAspect.identityMaps[itemSpec.type] = {}

            if results[i].serialNumber in IDIdentityMapAspect.identityMaps[itemSpec.type]:
                results[i] = IDIdentityMapAspect.identityMaps[itemSpec.type][results[i].serialNumber]

            else:
                IDIdentityMapAspect.identityMaps[itemSpec.type][results[i].serialNumber] = results[i]

        return results

    def delete_interceptor(original_function, serialNumber, type):
        # check if spec is already in identityMap, remove it if it is

        original_function(itemID)

        if type not in IDIdentityMapAspect.identityMaps:
            IDIdentityMapAspect.identityMaps[type] = {}

        if serialNumber in IDIdentityMapAspect.identityMaps[type]:
            IDIdentityMapAspect.identityMaps[type][serialNumber] = None

        return result

    def update_interceptor(original_function, itemID):
        # check if spec is already in identityMap, remove it if it is

        result = original_function(itemID)

        if itemID.spec.type not in IDIdentityMapAspect.identityMaps:
            IDIdentityMapAspect.identityMaps[itemID.spec.type] = {}

        if itemID.serialNumber in IDIdentityMapAspect.identityMaps[itemID.spec.type]:
            IDIdentityMapAspect.identityMaps[itemID.spec.type][itemID.serialNumber] = None

        return result


class PurchasedIdentityMapAspect:

    identityMap = dict()

    def find_interceptor(original_function, serialNumber):
        result = None

        # check if spec is already in identityMap
        if modelNumber in IDIdentityMapAspect.identityMap:
            result = PurchasedIdentityMapAspect.identityMap[serialNumber]

        # if it wasnt already read from the db, run regular find, store result and return it
        if result is None:
            result = original_function(serialNumber)

            PurchasedIdentityMapAspect.identityMap[serialNumber] = result

        return result

    def findByUser_interceptor(original_function, email):

        results = original_function(email)

        # insert unsaved results in the identity map, and replace newly loaded instance for previously loaded ones
        for i in range(0, len(results)):
            if results[i].serialNumber in PurchasedIdentityMapAspect.identityMap:
                results[i] = PurchasedIdentityMapAspect.identityMap[results[i].serialNumber]

            else:
                PurchasedIdentityMapAspect.identityMap[results[i].serialNumber] = results[i]

        return results

    def delete_interceptor(original_function, serialNumber):
        # check if spec is already in identityMap, remove it if it is

        original_function(serialNumber)

        if serialNumber in IDIdentityMapAspect.identityMap:
            IDIdentityMapAspect.identityMap[serialNumber] = None

        return result

    def update_interceptor(original_function, pruchasedItemID):
        # check if spec is already in identityMap, remove it if it is

        result = original_function(purchasedItemID)

        if purchasedItemID.serialNumber in IDIdentityMapAspect.identityMap:
            IDIdentityMapAspect.identityMap[purchasedItemID.serialNumber] = None

        return result
