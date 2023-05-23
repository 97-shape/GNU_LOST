from django.conf.urls.static import static
from django.urls import path

from config import settings
from postapp.views import list, create_post, filterdList, detail_post, filterdDetailList

app_name = 'postapp'

urlpatterns = [
    path('list/', list, name="list"),
    path('list/<str:filter>/', filterdList, name="filterd_list"),
    path('list/<str:category>/<str:type>', filterdDetailList, name="filtered_list"),
    path('create/', create_post, name="create"),
    path('detail/<int:post_id>', detail_post, name="detail")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)