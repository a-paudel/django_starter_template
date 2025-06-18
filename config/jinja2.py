from jinja2.environment import Environment
from django.templatetags.static import static
from django.urls import reverse as _django_reverse


def reverse(name, **kwargs):
    return _django_reverse(name, kwargs=kwargs)


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url_for": reverse,
        }
    )
    return env
