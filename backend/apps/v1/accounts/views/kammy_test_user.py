from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.utils.database import Database
from backend.apps.v1.accounts.serializers.user import UserSerializer
from backend.apps.v1.accounts.TDG.UserTDG import UserTDG
from backend.apps.v1.accounts.models.Customer import Customer

class Kam_Test_View(APIView):
    """
        API: users/
    """

    def get(self, request):
    	cus = Customer()
    	cus
        return Response()