from django.contrib import admin
from django.urls import path, include

from home.views import home_view

app_name = 'home'
urlpatterns = [
	path('', home_view, name='main'),

]
