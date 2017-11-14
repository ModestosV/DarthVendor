import uuid
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.utils.database import Database
from backend.apps.v1.accounts.serializers.user import UserSerializerLogin

from backend.apps.v1.accounts.ObjectSession import ObjectSession

from backend.apps.v1.accounts.Authentication import Authentication
from backend.apps.v1.accounts.models.Customer import Customer


class RegisterView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):

        email = request.data['email']
        password = request.data['password']
        username = request.data['username']
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        address = request.data['address']
        phone = request.data['phone']

        newCustomer = Customer(0,email,password,0,0,"",username,firstname,lastname,address,phone)
        valid = Authentication.register(newCustomer)
        if valid is False:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(userSerializer.data, status=status.HTTP_200_OK)
