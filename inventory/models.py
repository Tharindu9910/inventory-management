from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255)

    # Unique SKU is very important in inventory systems
    sku = models.CharField(max_length=100, unique=True)

    # Prevent negative stock at database + application level
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"