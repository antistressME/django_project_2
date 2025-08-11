from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from config.settings import BASE_DIR

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = BASE_DIR / "catalog/templates/home.html"
    context_object_name = "products"


class ContactsTemplateView(TemplateView):
    template_name = BASE_DIR / "catalog/templates/contacts.html"
    context_object_name = "contacts"


class ProductDetailView(DetailView):
    model = Product
    template_name = BASE_DIR / "catalog/templates/product_page.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = BASE_DIR / "catalog/templates/product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = BASE_DIR / "catalog/templates/product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    fields = ["name", "content", "image", "is_published"]
    template_name = BASE_DIR / "catalog/templates/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")
