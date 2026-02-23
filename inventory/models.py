from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255)

    sku = models.CharField(max_length=100, unique=True)#uniqueness

    quantity = models.IntegerField(
        validators=[MinValueValidator(0)]#minvalue validation
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"