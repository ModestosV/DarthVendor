from django.conf import settings
from django.conf.urls import url
from .views.login import LoginView
from .views.logout import LogoutView
from .views.admin import AdminView, AdminDetail 


urlpatterns = [

    # Login / Logout
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),

    url(r'^admins$', AdminView.as_view()),
    url(r'^admins/(?P<admin_id>[\d]+)$', AdminDetail.as_view()),
]