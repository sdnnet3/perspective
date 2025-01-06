from django.db import models
from modelcluster.fields import ParentalKey
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet
# Create your models here.



import requests
from bs4 import BeautifulSoup
from .utils import scrape_product_details

class ArtisticPrint(models.Model):
    payment_link = models.URLField(max_length=200, blank=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def fetch_print_info(self):
        info = scrape_product_details(self.payment_link)
        info['payment_link'] = self.payment_link
        return info

    panels = [
        FieldPanel('payment_link'),
        FieldPanel('name'),
    ]

