from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from config.settings import BASE_DIR

from .forms import ProductForm, ProductModeratorForm
from .models import Product


class ProductListView(ListView):
    """Класс контройлер для отображения списка продуктов."""

    model = Product
    template_name = BASE_DIR / "catalog/templates/home.html"
    context_object_name = "products"

    def get_queryset(self):
        # Возвращает только опубликованные продукты для обычных пользователей
        # и все продукты для модераторов продуктов
        queryset = super().get_queryset()
        user = self.request.user
        if user.has_perm("catalog.can_unpublish_product"):
            return queryset.filter()
        else:
            return queryset.filter(published=True)


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

    def form_valid(self, form):
        product = form.save(commit=False)
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс контройлер для обновления/изменения продукта."""

    model = Product
    form_class = ProductForm
    template_name = BASE_DIR / "catalog/templates/product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        # Предоставляет доступ к редастированию только для владельцев продуктов или модераторов
        user = self.request.user
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        if user == self.object.owner:
            return ProductForm
        raise PermissionDenied()


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Класс контройлер для удаления продукта."""

    model = Product
    fields = ["name", "content", "image", "is_published"]
    template_name = BASE_DIR / "catalog/templates/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        # Предоставляет доступ к удалению только для владельцев продуктов или модераторов
        user = self.request.user
        if (
            not user.has_perm("catalog.can_unpublish_product")
            or user != self.object.owner
        ):
            raise PermissionDenied()
