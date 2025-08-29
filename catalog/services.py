from django.core.cache import cache

from config.settings import CACHE_ENABLED

from .models import Product


class ProductService:
    @staticmethod
    def get_products_by_category(category_id):
        """Возвращает список продуктов указанной категории."""
        products = Product.objects.filter(category_id=category_id)
        return products

    @staticmethod
    def get_products_from_cache(category_id):
        """Кеширует список продуктов, отфильтрованных по категории."""
        if not CACHE_ENABLED:
            return ProductService.get_products_by_category(category_id)
        key = "product_list"
        products_cache = cache.get(key)
        if products_cache is not None:
            return products_cache
        products = ProductService.get_products_by_category(category_id)
        cache.set(key, products, 10)
        return products
