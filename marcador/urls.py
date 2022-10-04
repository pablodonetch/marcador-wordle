from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls import re_path as url
from django.conf import settings
from .views import HomeView, get_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    url(r'^api/data/$', get_data, name='api-data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)