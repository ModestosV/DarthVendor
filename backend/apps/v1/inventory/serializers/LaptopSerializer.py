from backend.apps.v1.inventory.serializers.AbstractSerializers import AbstractComputerSerializer
from backend.apps.v1.inventory.serializers.SizeSerializer import SizeSerializer

class LaptopSerializer(AbstractComputerSerializer):

    containCamera = AbstractComputerSerializer.BooleanField()
    isTouch = AbstractComputerSerializer.BooleanField()
    batteryInfo = AbstractComputerSerializer.CharField()
    os = AbstractComputerSerializer.CharField()
    size = SizeSerializer()