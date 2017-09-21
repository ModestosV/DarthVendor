from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.database import Database


class LogoutView(APIView):

    def get(self, request):
        """
            Remove API token. 
        """

        with Database() as cursor:
            query = """ 
                DELETE
                FROM token
                WHERE token = '{}'
            """.format(request.META['HTTP_AUTHORIZATION'])            

            try:
                cursor.execute(query)                    
            except Exception as error: 
                print(error) 
                return Response({}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({}, status=status.HTTP_200_OK)