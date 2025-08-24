from django.db import models

from users.models import User


class Category(models.Model):
    """Класс модели категории продукта."""

    name = models.CharField(
        null=False, blank=False, max_length=100, verbose_name="Наименование"
    )
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name  # стороковое отображение, например, в консоль

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]
        db_table = "custom_table_category"


class Product(models.Model):
    """Класс модели продукта."""

    name = models.CharField(
        null=False, blank=False, max_length=100, verbose_name="Наименование"
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    image = models.ImageField(
        null=True, blank=True, upload_to="images/", verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )
    price = models.FloatField(null=False, blank=False, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    published = models.BooleanField(default=False, verbose_name="Опубликовать")

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Автор",
    )

    def __str__(self):
        return f"{self.name}, цена: {self.price}"  # стороковое отображение, например, в консоль

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
        db_table = "custom_table_product"
        permissions = [
            ("can_unpublish_product", "Возможность отменять публикацию продукта"),
        ]
