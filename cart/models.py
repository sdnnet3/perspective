from django.db import models
from website.models import ImageProduct  # Ensure this import is here

class CartItem(models.Model):
    product = models.ForeignKey(ImageProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'

    @property
    def thumbnail(self):
        return self.product.thumbnail