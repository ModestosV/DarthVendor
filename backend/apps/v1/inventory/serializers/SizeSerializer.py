from rest_framework import serializers


class SizeSerializer(serializers.Serializer):
    size = serializers.FloatField()
    sizeFormat = serializers.CharField()
