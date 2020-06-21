from django.contrib import admin
from django.urls import path, include

from home.views import landing_view, about_us

urlpatterns = [
	path('', landing_view, name='landing'),
    path('home/', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('gallery/', include('gallery.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('about/', about_us, name='aboutme'),
    path('admin/', admin.site.urls),

]
