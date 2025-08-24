from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField

from .models import Product

# Определяем список запрещённых слов.
black_list_words = {
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
}


class StyleFormMixin:
    """Класс миксин для стилизации формы."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Класс формы для создания и обновления экземпляра класса Product."""

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"placeholder": "Введите наименование продукта"}
        )
        self.fields["description"].widget.attrs.update(
            {"placeholder": "Введите описание продукта"}
        )
        self.fields["price"].widget.attrs.update(
            {"placeholder": "Введите стоимость продукта"}
        )

    def clean_price(self):
        # Метод для проверки, что цена продукта не является отрицательным числом.
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной")
        return price

    def clean(self):
        # Метод для проверки названия и описания продукта на наличие запрещённых слов.
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        for word in black_list_words:
            if name and word in name.lower():
                self.add_error("name", "В названии продукта есть ошибка")
            if description and word in description.lower():
                self.add_error("description", "В описании продукта есть ошибка")

    class Meta:
        model = Product
        exclude = ("owner", "published")


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    """Класс формы для создания и обновления модератарами экземпляра класса Product."""

    class Meta:
        model = Product
        exclude = ("owner",)
