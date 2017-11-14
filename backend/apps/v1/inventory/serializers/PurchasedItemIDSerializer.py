from rest_framework import serializers

from backend.apps.v1.inventory.serializers.DesktopSerializer import DesktopSerializer
from backend.apps.v1.inventory.serializers.LaptopSerializer import LaptopSerializer
from backend.apps.v1.inventory.serializers.TabletSerializer import TabletSerializer
from backend.apps.v1.inventory.serializers.MonitorDisplaySerializer import MonitorDisplaySerializer


class PurchasedItemIDSerializer(serializers.Serializer):

    serialNumber = serializers.CharField()
    spec = serializers.SerializerMethodField()
    email = serializers.CharField()
    type = serializers.CharField()
    timeStamp = serializers.CharField()

    def get_spec(self, purchasedItemID):

        if purchasedItemID.type == "DESKTOP":
            return DesktopSerializer(purchasedItemID.spec).data
        elif purchasedItemID.type == "LAPTOP":
            return LaptopSerializer(purchasedItemID.spec).data
        elif purchasedItemID.type == "TABLET":
            return TabletSerializer(purchasedItemID.spec).data
        elif purchasedItemID.type == "MONITOR":
            return MonitorDisplaySerializer(purchasedItemID.spec).data
