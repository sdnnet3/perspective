from django.contrib import admin
from django.urls import path, include

from portfolio.views import portfolio_view, portfolio_profile

app_name = 'portfolio'

urlpatterns = [
	path('', portfolio_view, name='main'),
	path('<name>/', portfolio_profile, name='model'),
]
