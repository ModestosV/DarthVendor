from django.conf import settings
from django.db import connection
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlite3 import dbapi2 as Database


class AdminView(APIView):
    """
        API: admins/
    """

    def get(self, request):
        """
            List admins.
        """

        return Response(dict(test="hi"))