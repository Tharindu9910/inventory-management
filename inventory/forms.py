from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "sku", "quantity", "price"]

    # Prevent negative quantity
    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")

        if quantity is None:
            raise forms.ValidationError("Quantity is required.")

        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative.")

        return quantity

    # Prevent negative price
    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price is None:
            raise forms.ValidationError("Price is required.")

        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")

        return price