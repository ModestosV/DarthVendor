from django.conf import settings
from django.conf.urls import url
from .views.admin import AdminView


urlpatterns = [
    url(r'^admins$', AdminView.as_view())
]