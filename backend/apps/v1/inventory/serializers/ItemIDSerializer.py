from backend.v1.inventory.serializers.DesktopSerializer import DesktopSerializer
from backend.v1.inventory.serializers.LaptopSerializer import LaptopSerializer
from backend.v1.inventory.serializers.TabletSerializer import TabletSerializer
from backend.v1.inventory.serializers.MonitorDisplaySerializer import MonitorDisplaySerializer

from rest_framework import serializers


class ItemIDSerialzer(serializers.Serializer):
    serialNumber = serializers.CharField()
    isLocked = serializers.BooleanField()
    itemSpec = serializers.SerializerMethodField()

    def get_itemSpec(self, itemID):

        if itemID.spec.type == "DESKTOP":
            return DesktopSerializer()
        elif itemID.spec.type == "LAPTOP":
            return LaptopSerializer()
        elif itemID.spec.type == "TABLET":
            return TabletSerializer()
        else itemID.spec.type == "MONITOR":
            return MonitorDisplaySerializer()
