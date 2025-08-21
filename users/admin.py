from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс отображения пользователей в админке"""

    exclude = ("password",)
    search_fields = ("name",)
