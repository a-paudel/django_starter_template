from django.shortcuts import render
from django.contrib.auth.views import LoginView as _DjangoLoginView

from users.forms import LoginForm

# Create your views here.


class LoginView(_DjangoLoginView):
    form_class = LoginForm
    template_name = "users/auth/login.html"
    redirect_authenticated_user = True
