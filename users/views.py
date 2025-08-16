from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import BASE_DIR, EMAIL_HOST_USER

from .forms import UserRegisterForm
from .models import User


class RegisterUserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = BASE_DIR / "users/templates/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        recipient_list = [user_email]
        from_email = EMAIL_HOST_USER
        send_mail(subject, message, from_email, recipient_list)
