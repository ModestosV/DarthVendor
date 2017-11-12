from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.utils.database import Database

from backend.apps.v1.accounts.ObjectSession import ObjectSession


class LogoutView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        """
            Logout
        """

        ObjectSession.sessions[request.session['user']] = None
        request.session['user'] = None

        return Response({}, status=status.HTTP_200_OK)
