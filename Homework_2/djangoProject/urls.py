
from django.contrib import admin
from django.urls import path
from .views import search_title


urlpatterns = [path('search_title/', search_title), path('admin/', admin.site.urls)]
