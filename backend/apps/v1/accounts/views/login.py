import uuid
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.db import connection
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlite3 import dbapi2 as Database
from utils.database import dict_factory
from backend.apps.v1.accounts.serializers.admin import AdminSerializerLogin


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
            serializer = AdminSerializerLogin(data=user)                        
           
            if not serializer.is_valid():
                connection.close()
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            

            if not check_password(request.data.get('password'), user["password"]):
                connection.close()
                return Response('Invalid username/password.', status=status.HTTP_400_BAD_REQUEST)

            token = serializer.data["token"]

            # Create token if does not exist
            if not bool(token):
                token = str(uuid.uuid4()).replace('-','')
                query = """
                    INSERT INTO token (token, admin_id)
                    VALUES (                
                        '{}',
                        {}
                    );
                """.format(token, serializer.data['id'])            

                cursor.execute(query)                   
                serializer = AdminSerializerLogin(serializer.data)
                connection.commit()

        except Exception as error: 
            print(error) 
            connection.close()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        connection.close()
        return Response(serializer.data, status=status.HTTP_200_OK)
        