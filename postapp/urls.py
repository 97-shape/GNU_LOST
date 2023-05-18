from django.conf.urls.static import static
from django.urls import path

from config import settings
from postapp.views import displayDetail, list, create_post

urlpatterns = [
    path('id/', displayDetail, name="detail"),
    path('list/', list, name="list"),
    path('create/', create_post, name="create")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)