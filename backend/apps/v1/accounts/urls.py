from django.conf.urls import url
from .views.login import LoginView
from .views.logout import LogoutView
from .views.user import UserView, UserDetail
from .views.register import RegisterView
from .views.viewCustomers import ViewCustomerView
from .views.deleteAccount import DeleteAccountView


urlpatterns = [

    # Login / Logout
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),

    url(r'^users$', UserView.as_view()),
    url(r'^users/(?P<user_id>[\d]+)$', UserDetail.as_view()),
    url(r'^register$', RegisterView.as_view()),
    url(r'^viewCustomers$', ViewCustomerView.as_view()),
    url(r'^deleteAccount$', DeleteAccountView.as_view())
]
