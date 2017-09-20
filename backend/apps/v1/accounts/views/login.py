from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.db import connection
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlite3 import dbapi2 as Database
from utils.database import dict_factory
from backend.apps.v1.accounts.serializers.admin import AdminSerializer


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        """
            Get user data and API token.
        """
        
        connection = Database.connect(settings.DATABASES['default']['NAME'])
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        query = """
            SELECT *
            FROM administrator
            WHERE username='{}'
        """.format(request.data.get('username'))

        try:
            cursor.execute(query)    
            user = cursor.fetchone()
            serializer = AdminSerializer(data=user)            

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if not check_password(request.data.get('password'), user["password"]):
                return Response('Invalid username/password.', status=status.HTTP_400_BAD_REQUEST)

        except Exception as error: 
            print(error) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)
        