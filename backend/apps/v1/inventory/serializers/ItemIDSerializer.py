from backend.apps.v1.inventory.serializers.DesktopSerializer import DesktopSerializer
from backend.apps.v1.inventory.serializers.LaptopSerializer import LaptopSerializer
from backend.apps.v1.inventory.serializers.TabletSerializer import TabletSerializer
from backend.apps.v1.inventory.serializers.MonitorDisplaySerializer import MonitorDisplaySerializer

from rest_framework import serializers


class ItemIDSerializer(serializers.Serializer):
    serialNumber = serializers.CharField()
    isLocked = serializers.BooleanField()
    itemSpec = serializers.SerializerMethodField()

    def get_itemSpec(self, itemID):

        if itemID.spec.type == "DESKTOP":
            return DesktopSerializer(itemID.spec).data
        elif itemID.spec.type == "LAPTOP":
            return LaptopSerializer(itemID.spec).data
        elif itemID.spec.type == "TABLET":
            return TabletSerializer(itemID.spec).data
        elif itemID.spec.type == "MONITOR":
            return MonitorDisplaySerializer(itemID.spec).data
