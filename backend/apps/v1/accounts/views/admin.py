from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.utils.database import Database
from backend.apps.v1.accounts.serializers.admin import AdminSerializer


class AdminView(APIView):
    """
        API: admins/
    """

    def get(self, request):
        """
            List admins.
        """

        with Database() as cursor: 
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


class AdminDetail(APIView):
    """
        API: admins/{admin_id}
    """

    def get(self, request, admin_id):
        """
            View individual admin.
        """

        with Database() as cursor: 
            query = """
                SELECT *
                FROM administrator
                WHERE id={}
            """.format(admin_id)

            try:
                cursor.execute(query)            
                serializer = AdminSerializer(data=cursor.fetchall(), many=True)

                if not serializer.is_valid():                    
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Exception as error: 
                print(error)                 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        
        return Response(serializer.data, status=status.HTTP_200_OK)
