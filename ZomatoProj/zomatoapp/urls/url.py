from django.urls import path, include
from ZomatoProj.constants import *
from ..views.user import UserListView

urlpatterns = [
    path(USERS, UserListView.as_view()),
]