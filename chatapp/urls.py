# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:room_id>/", views.chatroom_detail, name="room"),
    path("list/", views.room_list, name="list"),
    path("create_room/<int:writer_id>", views.create_chatroom, name="create_room"),
    path("find_room/<int:writer_id>", views.chatroom_create_or_join, name="find_room")
]