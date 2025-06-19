from django.contrib.auth.forms import (
    AuthenticationForm as _DjangoLoginForm,
    UserCreationForm as _DjangoRegisterForm,
)

from core.forms import BaseForm
from users.models import User


class LoginForm(BaseForm, _DjangoLoginForm):
    pass


class RegisterForm(BaseForm, _DjangoRegisterForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
