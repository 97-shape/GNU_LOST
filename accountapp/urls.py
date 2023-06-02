from django.urls import path

from accountapp.views import myaccount, login, need_login

app_name = "accountapp"

urlpatterns = [
    path("myaccount/", myaccount, name="myaccount"),
    path("login/", login, name="login"),
    path("need_login/", need_login, name="need_login"),
]