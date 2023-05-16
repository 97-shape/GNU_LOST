from django.urls import path

from accountapp.views import myaccount, login

app_name = "accountapp"

urlpatterns = [
    path("myaccount/", myaccount, name="myaccount"),
    path("login/", login, name="login"),
]