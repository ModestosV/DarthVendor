import uuid
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.utils.database import Database
from backend.apps.v1.accounts.serializers.user import UserSerializerLogin

from backend.apps.v1.inventory.ItemAdministration import ItemAdministration
from backend.apps.v1.accounts.ObjectSession import ObjectSession

from backend.apps.v1.accounts.Authentication import Authentication
from backend.apps.v1.accounts.models.Customer import Customer


class viewCustomerView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        
        customers = Authentication.viewAllCustomer()

        return Response({}, status=status.HTTP_200_OK)