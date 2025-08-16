from django.urls import path

from blog.apps import BlogConfig

from .views import (
    BlogNoteCreateView,
    BlogNoteDeleteView,
    BlogNoteDetailView,
    BlogNoteListView,
    BlogNoteUpdateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("blog/", BlogNoteListView.as_view(), name="blog"),
    path("blog/<int:pk>/", BlogNoteDetailView.as_view(), name="blog_note"),
    path("blog/blog_form", BlogNoteCreateView.as_view(), name="blog_form"),
    path("blog/update/<int:pk>/", BlogNoteUpdateView.as_view(), name="blog_update"),
    path("blog/delete/<int:pk>/", BlogNoteDeleteView.as_view(), name="confirm_delete"),
]
