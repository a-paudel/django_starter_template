from django.contrib.auth.forms import AuthenticationForm as _DjangoLoginForm

from core.forms import BaseForm


class LoginForm(BaseForm, _DjangoLoginForm):
    pass
