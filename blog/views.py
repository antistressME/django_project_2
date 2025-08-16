from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from config.settings import BASE_DIR

from .models import BlogNote


class BlogNoteListView(ListView):
    """Класс контройлер для отображения списка блоговых записей."""

    model = BlogNote
    template_name = BASE_DIR / "blog/templates/blog.html"
    context_object_name = "blogs"

    def get_queryset(self):
        # Возвращает только опубликованные блоговые записи
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogNoteDetailView(DetailView):
    """Класс контройлер для отображения деталей блоговой записи."""

    model = BlogNote
    template_name = BASE_DIR / "blog/templates/blog_note.html"
    context_object_name = "blog_note"

    def get_object(self, queryset=None):
        # Метод для подсчёта просмотров
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogNoteCreateView(CreateView):
    """Класс контройлер для создания блоговой записи."""

    model = BlogNote
    fields = ["name", "content", "image", "is_published"]
    template_name = BASE_DIR / "blog/templates/blog_form.html"
    context_object_name = "blog_note"
    success_url = reverse_lazy("blog:blog")


class BlogNoteUpdateView(UpdateView):
    """Класс контройлер для изменения/обновления блоговой записи."""

    model = BlogNote
    fields = ["name", "content", "image", "is_published"]
    template_name = BASE_DIR / "blog/templates/blog_form.html"
    context_object_name = "blog_note"
    success_url = reverse_lazy("blog:blog")

    def get_success_url(self):
        # Перенаправляет на созданную блоговую запись
        return reverse("blog:blog_note", args=[self.kwargs.get("pk")])


class BlogNoteDeleteView(DeleteView):
    """Класс контройлер для удаления блоговой записи."""

    model = BlogNote
    template_name = BASE_DIR / "blog/templates/blog_confirm_delete.html"
    context_object_name = "blog_note"
    success_url = reverse_lazy("blog:blog")
