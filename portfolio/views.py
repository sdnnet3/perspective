from django.shortcuts import render
from .models import Profiles

# Create your views here.
def portfolio_view(request, *args, **kwargs):
	profiles = Profiles.objects.all()
	context = {"active_portfolio":'class=active', "profiles":profiles}
	return render(request, "portfolio_striped.html", context)

def portfolio_profile(request, name, *args, **kwargs):
	profiles = Profiles.objects.get(name=name)
	context = {"profiles":profiles}
	return render(request, "portfolio_single_2.html", context)