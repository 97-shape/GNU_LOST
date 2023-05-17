from django.urls import path

from postapp.views import displayDetail, test, create_post

urlpatterns = [
    path('id/', displayDetail, name="detail"),
    path('test/', test, name="test"),
    path('create/', create_post, name="create")
]