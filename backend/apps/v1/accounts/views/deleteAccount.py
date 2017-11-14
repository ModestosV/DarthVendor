from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.utils.database import Database

from backend.apps.v1.accounts.ObjectSession import ObjectSession
from backend.apps.v1.accounts.Authentication import Authentication


class DeleteAccountView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):

        if not Authentication.deleteCustomer(request.session['user']):
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            ObjectSession.sessions[request.session['user']] = None
            request.session['user'] = None
            request.session['isAdmin'] = None

        return Response({}, status=status.HTTP_200_OK)
