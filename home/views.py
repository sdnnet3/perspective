from django.shortcuts import render
from home.models import Layout, About

# Create your views here.
def landing_view(request, *args, **kwargs):
	layouts = Layout.objects.all()
	context = {"layouts":layouts}
	return render(request, "home_landing_striped_pages.html", context)

def home_view(request, *args, **kwargs):
	context = {"active_home":'class=active'}
	return render(request, "index.html", context)

def about_us(request, *args, **kwargs):
	about = About.objects.all()
	context = {"about":about, "active_about":'class=active'}
	return render(request, "page_about_me.html", context)