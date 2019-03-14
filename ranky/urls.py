from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('instashot.urls')),
]
