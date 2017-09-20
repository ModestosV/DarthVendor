from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    id = serializers.HiddenField(default='')
    token = serializers.CharField(max_length=255)
    admin_id = serializers.HiddenField(default='')
