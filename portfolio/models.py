from django.db import models

# Create your models here.
class Profiles(models.Model):
	name = models.CharField(max_length=50)
	stripe = models.ImageField(default='default.png', blank=True)
	full = models.ImageField(blank=True, null=True)
	full2 = models.ImageField(blank=True, null=True)
	full3 = models.ImageField(blank=True, null=True)
	message = models.TextField(default='', blank=True)
	client = models.CharField(max_length=50, default='')
	photographer = models.CharField(max_length=30, default='')
	camera = models.CharField(max_length=20, default='')
	date = models.DateField(auto_now=False, default='2020-03-10')
	social = models.CharField(max_length=100, default='')
	featureImg = models.ImageField(default='default.png', blank=True)
	featureInfo = models.TextField(default='', blank=True)

	def __str__(self):
		return self.name