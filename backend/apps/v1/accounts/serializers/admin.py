from django.conf import settings
from django.db import connection
from rest_framework import serializers
from sqlite3 import dbapi2 as Database
from utils.database import dict_factory
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
        connection = Database.connect(settings.DATABASES['default']['NAME'])
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        query = """
            SELECT *
            FROM token
            WHERE admin_id={}
        """.format(admin["id"])

        try:
            cursor.execute(query)    
            admin = cursor.fetchone()
            return admin["token"]
        except Exception as error: 
            return None

