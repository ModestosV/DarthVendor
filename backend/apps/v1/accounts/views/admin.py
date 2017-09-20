from django.conf import settings
from django.db import connection
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlite3 import dbapi2 as Database
from utils.database import dict_factory
from backend.apps.v1.accounts.serializers.admin import AdminSerializer


class AdminView(APIView):
    """
        API: admins/
    """

    def get(self, request):
        """
            List admins.
        """

        connection = Database.connect(settings.DATABASES['default']['NAME'])
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        query = """
            SELECT *
            FROM administrator
        """

        try:
            cursor.execute(query)            
            serializer = AdminSerializer(data=cursor.fetchall(), many=True)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error: 
            print(error) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

