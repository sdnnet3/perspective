from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from gallery.views import gallery_view

app_name = 'gallery'
urlpatterns = [
	path('', gallery_view, name='main'),

]