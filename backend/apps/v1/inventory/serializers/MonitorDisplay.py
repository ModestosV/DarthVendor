from backend.apps.v1.inventory.serializers.AbstractSerializers import ItemSpecificationSerializer
from backend.apps.v1.inventory.serializers.SizeSerializer import SizeSerializer

class LaptopSerializer(ItemSpecificationSerializer):
    size = SizeSerializer()