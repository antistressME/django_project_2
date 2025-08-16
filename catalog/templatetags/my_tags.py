from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    """Фильтр для обработки пути к изображению в шаблонах."""
    if path:
        return f"/media/{path}"
    return "#"
