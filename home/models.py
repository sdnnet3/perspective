from django.db import models

# Create your models here.

class Layout(models.Model):
	Home = models.ImageField(default='default.png', blank=True)
	Gallery = models.ImageField(default='default.png', blank=True)
	Portfolio = models.ImageField(default='default.png', blank=True)
	Logo = models.ImageField(default='default.png', blank=True)

class About(models.Model):
	name = models.CharField(max_length=30)
	place = models.CharField(max_length=30)
	work = models.CharField(max_length=30)
	title = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	mainImg = models.ImageField(default='default.png', blank=True)
	sideImg = models.ImageField(default='default.png', blank=True)
	facebook = models.CharField(max_length=60)
	instagram = models.CharField(max_length=60)
	bio = models.TextField(default='')

	def __str__(self):
		return self.name