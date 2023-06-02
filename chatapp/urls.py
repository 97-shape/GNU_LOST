# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:room_id>/", views.chatroom_detail, name="room"),
    path("create_room/", views.create_chatroom, name="create_room")
]