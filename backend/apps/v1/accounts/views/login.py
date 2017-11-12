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


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):

        isAdmin = request.data['isAdmin']

        email = request.data['email']
        password = request.data['password']

        if isAdmin is False:
            user = Authentication.customerLogin(email, password)

        else:
            user = Authentication.adminLogin(email, password)

        if user is None:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)

        request.session['user'] = email
        ObjectSession.session[email] = user

        userSerializer = UserSerializerLogin(user)

        if not userSerializer.is_valid():
            return Respoonse(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(userSerializer.data, status=status.HTTP_200_OK)
