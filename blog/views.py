from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_view(request, *args, **kwargs):
	context = {"active_blog":'class=active'}
	return render(request, "blog_fullwidth_2.html", context)

def post_view(request, *args, **kwargs):
	context = {}
	return render(request, "blog_single_fullwidth.html", context)