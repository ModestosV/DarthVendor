from backend.apps.v1.inventory.serializers.AbstractSerializers import ItemSpecificationSerializer


class MonitorDisplaySerializer(ItemSpecificationSerializer):
    size = serializers.FloatField()
    sizeFormat = serializers.CharField()
