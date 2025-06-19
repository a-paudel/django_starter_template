from django.shortcuts import render
from django.contrib.auth.views import LoginView as _DjangoLoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import LoginForm, RegisterForm
from users.models import User

# Create your views here.


class LoginView(_DjangoLoginView):
    form_class = LoginForm
    template_name = "users/auth/login.html"
    redirect_authenticated_user = True


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = "users/auth/register.html"
    success_url = reverse_lazy("users:login")
    success_message = "Account created successfully. You can now log in."
