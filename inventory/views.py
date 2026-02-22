from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy,reverse
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect, get_object_or_404
from .services import update_stock
from django.contrib import messages
from django.core.exceptions import ValidationError


class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"
    context_object_name = "products"
    ordering = ["-created_at"]


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/product_form.html"
    success_url = reverse_lazy("product-list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/product_form.html"
    success_url = reverse_lazy("product-list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "inventory/product_confirm_delete.html"
    success_url = reverse_lazy("product-list")
    

class ProductStockUpdateView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        change_amount = int(request.POST.get("change_amount", 0))

        try:
            update_stock(product.id, change_amount)
            messages.success(request, "Stock updated successfully.")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect(reverse("product-list"))