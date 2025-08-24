from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """Класс создание кастомной кансольной команды для добавления тестовых продуктов."""

    help = "Add test products to the database"

    def handle(self, *args, **kwargs):

        category1, _ = Category.objects.get_or_create(name="vegetables")
        category2, _ = Category.objects.get_or_create(name="fruits")
        category3, _ = Category.objects.get_or_create(name="berries")

        products = [
            {
                "name": "raspberry",
                "description": "test",
                "category": category3,
                "price": "350",
            },
            {
                "name": "carrot",
                "description": "test",
                "category": category1,
                "price": "55",
            },
            {
                "name": "pear",
                "description": "test",
                "category": category2,
                "price": "239",
            },
            {
                "name": "strawberry",
                "description": "test",
                "category": category3,
                "price": "299",
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added product: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exists: {product.name}")
                )
