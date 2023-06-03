# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("guide", views.guide, name="guide"),
    path("qna", views.qna, name="qna"),
    path("ask", views.ask, name="ask"),
]