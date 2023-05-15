from django.urls import path

from postapp.views import displayDetail

urlpatterns = [
    path('id/', displayDetail, name="detail")
]