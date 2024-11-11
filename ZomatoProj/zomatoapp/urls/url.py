from django.urls import path, include
from ZomatoProj.constants import *
from ..views.user import UserListView
from ..views.orders import OrderItemsView

urlpatterns = [
    path(USERS, UserListView.as_view()),
    path(USERS_BY_ID, UserListView.as_view()),
    path(ORDER_ITEMS, OrderItemsView.as_view()),
]
