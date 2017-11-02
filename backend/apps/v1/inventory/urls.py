from django.conf import settings
from django.conf.urls import url
from .views.inventory import InventoryView
from .views.item import ItemView
from .views.andres import AndresView


urlpatterns = [
    url(r'^inventory$', InventoryView.as_view()),
    url(r'^item', ItemView.as_view()),
    url(r'^andres', AndresView.as_view())
]
