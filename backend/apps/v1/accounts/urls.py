from django.conf import settings
from django.conf.urls import url
from .views.admin import AdminView, AdminDetail 


urlpatterns = [
    url(r'^admins$', AdminView.as_view()),
    url(r'^admins/(?P<admin_id>[\d]+)$', AdminDetail.as_view()),
]