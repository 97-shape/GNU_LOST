from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

import accountapp.views
from homeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homeapp.urls')),
    path('post/', include('postapp.urls')),
    path('account/', include('accountapp.urls')),
    path('', accountapp.views.login, name='login'),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)