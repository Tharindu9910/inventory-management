from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Product


def update_stock(product_id: int, change_amount: int):
    """
    Safely increase or decrease product stock.
    Prevents race conditions using row-level locking.
    """

    with transaction.atomic():
        # Lock row until transaction completes
        product = Product.objects.select_for_update().get(id=product_id)

        new_quantity = product.quantity + change_amount

        if new_quantity < 0:
            raise ValidationError("Stock cannot go below zero.")

        product.quantity = new_quantity
        product.save()

        return product