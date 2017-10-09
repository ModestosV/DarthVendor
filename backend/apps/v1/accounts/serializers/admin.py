from rest_framework import serializers
from backend.utils.database import Database
from .token import TokenSerializer


class AdminSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    password = serializers.HiddenField(default='')


class AdminSerializerLogin(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    password = serializers.HiddenField(default='')
    token = serializers.SerializerMethodField()

    def get_token(self, admin):
        with Database() as cursor:
            query = """
                SELECT *
                FROM token
                WHERE user_id={}
            """.format(admin["id"])

            try:
                cursor.execute(query)
                admin = cursor.fetchone()
                return admin["token"]
            except Exception as error:
                print(error)
                return None
