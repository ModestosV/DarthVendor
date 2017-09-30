import uuid
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.utils.database import Database
from backend.apps.v1.accounts.serializers.admin import AdminSerializerLogin


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        """
            Get user data and API token.
        """
        
        with Database() as cursor:
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
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            

                if not check_password(request.data.get('password'), user["password"]):
                    return Response('Invalid username/password.', status=status.HTTP_400_BAD_REQUEST)

                token = serializer.data["token"]

                # Create token if does not exist
                if not bool(token):
                    token = str(uuid.uuid4()).replace('-','')
                    query = """
                        INSERT INTO token (token, admin_id)
                        VALUES ('{}', {});
                    """.format(token, serializer.data['id'])            

                    cursor.execute(query)                   
                    serializer = AdminSerializerLogin(serializer.data)

            except Exception as error: 
                print(error) 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.data, status=status.HTTP_200_OK)
        