from typing import Any
from django.contrib.auth.views import LoginView as _DjangoLoginView
from django.urls import NoReverseMatch, reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from users.forms import LoginForm, RegisterForm

# Create your views here.


class LoginView(_DjangoLoginView):
    form_class = LoginForm
    template_name = "users/auth/login.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        try:
            reverse("users:register")
            kwargs["has_register_page"] = True
        except NoReverseMatch:
            kwargs["has_register_page"] = False

        return super().get_context_data(**kwargs)


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = "users/auth/register.html"
    success_url = reverse_lazy("users:login")
    success_message = "Account created successfully. You can now log in."
