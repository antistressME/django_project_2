from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from config.settings import BASE_DIR

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    """Класс контройлер для отображения списка продуктов."""

    model = Product
    template_name = BASE_DIR / "catalog/templates/home.html"
    context_object_name = "products"


class ContactsTemplateView(TemplateView):
    """Класс контройлер для отображения контактов."""

    template_name = BASE_DIR / "catalog/templates/contacts.html"
    context_object_name = "contacts"


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Класс контройлер для отображения деталей продукта."""

    model = Product
    template_name = BASE_DIR / "catalog/templates/product_page.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс контройлер для создания продукта."""

    model = Product
    form_class = ProductForm
    template_name = BASE_DIR / "catalog/templates/product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс контройлер для обновления/изменения продукта."""

    model = Product
    form_class = ProductForm
    template_name = BASE_DIR / "catalog/templates/product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Класс контройлер для удаления продукта."""

    model = Product
    fields = ["name", "content", "image", "is_published"]
    template_name = BASE_DIR / "catalog/templates/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")
