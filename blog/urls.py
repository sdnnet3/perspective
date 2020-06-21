from django.contrib import admin
from django.urls import path

from .views import blog_view, post_view

app_name = 'blog'
urlpatterns = [
	path('', blog_view, name='index'),
	path('post/', post_view, name='post'),
    # path('', _view, name=''),
]
