from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.utils.database import Database
from backend.apps.v1.accounts.serializers.user import UserSerializer


class UserView(APIView):
    """
        API: users/
    """

    def get(self, request):
        """
            List users.
        """

        with Database() as cursor:
            query = """
                SELECT *
                FROM user
            """

            try:
                cursor.execute(query)     
                serializer = UserSerializer(data=cursor.fetchall(), many=True)

                if not serializer.is_valid():                    
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Exception as error: 
                print(error)                 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetail(APIView):
    """
        API: users/{user_id}
    """

    def get(self, request, user_id):
        """
            View individual user.
        """

        with Database() as cursor:
            query = """
                SELECT *
                FROM user
                WHERE id={}
            """.format(user_id)

            try:
                cursor.execute(query)
                serializer = UserSerializer(data=cursor.fetchall(), many=True)

                if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Exception as error:                 
                print(error)                 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        
        return Response(serializer.data, status=status.HTTP_200_OK)
