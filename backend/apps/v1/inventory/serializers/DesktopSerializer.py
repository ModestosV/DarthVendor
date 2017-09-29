from backend.apps.v1.inventory.serializers.AbstractSerializers import AbstractComputerSerializer
from backend.apps.v1.inventory.serializers.DimensionSerializer import DimensionSerializer


class DesktopSerializer(AbstractComputerSerializer):
    dimension = DimensionSerializer()