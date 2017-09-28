from django.conf import settings
from django.conf.urls import url
from .views.inventory import InventoryView

urlpatterns = [
    url(r'^inventory$', InventoryView.as_view()),
]
