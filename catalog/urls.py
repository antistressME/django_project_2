from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig

from .views import (CategoryProductView, ContactsTemplateView,
                    ProductCreateView, ProductDeleteView, ProductDetailView,
                    ProductListView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path(
        "product_page/<int:pk>/",
        cache_page(6)(ProductDetailView.as_view()),
        name="product_page",
    ),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("products/new/", ProductCreateView.as_view(), name="product_form"),
    path(
        "products/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "products/category/<int:pk>/",
        CategoryProductView.as_view(),
        name="category_products",
    ),
]
