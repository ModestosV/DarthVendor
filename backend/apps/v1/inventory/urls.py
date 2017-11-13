from django.conf import settings
from django.conf.urls import url
from .views.inventory import InventoryView
from .views.item import AddItemSpecView, InitiateEdit, TerminateEdit, CancelEditView, ModifyItemSpecView, getEditStateView, AddQuantityView
from .views.itemID import ItemIDsForSpecView, DeleteItemID
from .views.purchase import CartView, AddToCartView, RemoveFromCartView


urlpatterns = [
    url(r'^inventory$', InventoryView.as_view()),
    url(r'^addItemSpec', AddItemSpecView.as_view()),
    url(r'^modifyItemSpec', ModifyItemSpecView.as_view()),
    url(r'^addQuantity', AddQuantityView.as_view()),
    url(r'^initiateEdit', InitiateEdit.as_view()),
    url(r'^terminateEdit', TerminateEdit.as_view()),
    url(r'^cancelEdit', CancelEditView.as_view()),
    url(r'^getEditState', getEditStateView.as_view()),
    url(r'^getItemIDs', ItemIDsForSpecView.as_view()),
    url(r'^deleteItemID', DeleteItemID.as_view()),
    url(r'^viewCart', CartView.as_view()),
    url(r'^addToCart', AddToCartView.as_view()),
    url(r'^removeFromCart', RemoveFromCartView.as_view())
]
