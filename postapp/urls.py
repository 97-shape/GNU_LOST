from django.conf.urls.static import static
from django.urls import path

from config import settings
from postapp.views import displayDetail, list, create_post, filterdList

app_name = 'postapp'

urlpatterns = [
    path('id/', displayDetail, name="detail"),
    path('list/', list, name="list"),
    path('list/<str:category>/<str:type>', filterdList, name="filtered_list"),
    path('create/', create_post, name="create")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)