from django.db import models


class BlogNote(models.Model):
    """Класс модели для создания блоговой записи"""

    name = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")

    image = models.ImageField(
        null=True, blank=True, upload_to="images/", verbose_name="Превью (изображение)"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    is_published = models.BooleanField(default=False, verbose_name="Опубликовать")

    views_counter = models.PositiveIntegerField(
        default=0, verbose_name="количество просмотров"
    )

    def __str__(self):
        return self.name  # стороковое отображение, например, в консоль

    class Meta:
        verbose_name = "блоговая запись"
        verbose_name_plural = "блоговые записи"
        ordering = ["name"]
        db_table = "custom_table_blog_notes"
