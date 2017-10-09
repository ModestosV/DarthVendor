from django.conf.urls import url
from .views.login import LoginView
from .views.logout import LogoutView
from .views.user import UserView, UserDetail


urlpatterns = [

    # Login / Logout
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),

    url(r'^users$', UserView.as_view()),
    url(r'^users/(?P<user_id>[\d]+)$', UserDetail.as_view()),
]
