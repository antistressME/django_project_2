from django.urls import path

from catalog.apps import CatalogConfig

from .views import (ContactsTemplateView, ProductCreateView, ProductDeleteView,
                    ProductDetailView, ProductListView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("product_page/<int:pk>/", ProductDetailView.as_view(), name="product_page"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("product/new/", ProductCreateView.as_view(), name="product_form"),
    path(
        "product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
]
