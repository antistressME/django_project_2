from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin

from .models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Класс форма для регистрации пользователя."""

    class Meta:
        model = User
        fields = ("email", "password1", "password2")
