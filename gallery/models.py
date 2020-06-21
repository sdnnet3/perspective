from django.db import models

# Create your models here.


class Photo(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)
	full_size = models.ImageField(default='default.png', blank=True)
	thumb = models.ImageField(default='default.png', blank=True)
	weddings = models.BooleanField(default=False)
	families = models.BooleanField(default=False)
	indoors = models.BooleanField(default=False)
	outdoors = models.BooleanField(default=False)
	portraits = models.BooleanField(default=False)
	fashion = models.BooleanField(default=False)
	social = models.CharField(max_length=100)

	def __str__(self):
		return self.title