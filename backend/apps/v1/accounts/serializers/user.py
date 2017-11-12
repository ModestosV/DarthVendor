from rest_framework import serializers
from backend.utils.database import Database
from .token import TokenSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    password = serializers.HiddenField(default='')
    isAdmin = serializers.BooleanField(default='')


class UserSerializerLogin(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    password = serializers.HiddenField(default='')
    isAdmin = serializers.BooleanField(default='')
    token = serializers.SerializerMethodField()
    adminPermission = serializers.BooleanField(default=False)

    def get_token(self, user):
        with Database() as cursor:
            query = """
                SELECT *
                FROM token
                WHERE user_id={}
            """.format(user["id"])

            try:
                cursor.execute(query)
                user = cursor.fetchone()                
                return user["token"] if user else None
            except Exception as error:
                print(error)
                return None
