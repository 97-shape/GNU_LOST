from django.urls import path

from accountapp.views import login

urlpatterns = [
    path("login/", login, name="login"),

]