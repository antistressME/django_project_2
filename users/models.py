from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(
        max_length=11,
        verbose_name="Номер телефона",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=65,
        verbose_name="Страна",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/",
        verbose_name="Аватар пользователя (изображение)",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользовватель"
        verbose_name_plural = "Пользовватели"

    def __str__(self):
        return self.email
