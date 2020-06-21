from django.http import HttpResponse
from django.shortcuts import render
from .models import Photo

# Create your views here.
def gallery_view(request, *args, **kwargs):
	photos = Photo.objects.all()
	context = {"active_gallery":'class=active',
			"photos":photos}
	return render(request, "gallery_isotope_masonry.html", context)

# Create your views here.
