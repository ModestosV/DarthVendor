from django.conf import settings
from django.conf.urls import url
from .views.inventory import InventoryView
from .views.item import AddItemSpecView, InitiateEdit, TerminateEdit, ModifyItemSpecView, getEditStateView


urlpatterns = [
    url(r'^inventory$', InventoryView.as_view()),
    url(r'^addItemSpec', AddItemSpecView.as_view()),
    url(r'^modifyItemSpec', ModifyItemSpecView.as_view()),
    url(r'^initiateEdit', InitiateEdit.as_view()),
    url(r'^terminateEdit', TerminateEdit.as_view()),
    url(r'^getEditState', getEditStateView.as_view())
]
