from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.v1.inventory.models.Store


class ItemView(APIView):

    def post(self, request):
        
