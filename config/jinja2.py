from jinja2.environment import Environment
from django.templatetags.static import static
from django.urls import reverse as _django_reverse
from django_vite.templatetags.django_vite import vite_hmr_client, vite_asset, vite_asset_url


def reverse(name, **kwargs):
    return _django_reverse(name, kwargs=kwargs)


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url_for": reverse,
            "vite_hmr_client": vite_hmr_client,
            "vite_asset": vite_asset,
            "vite_asset_url": vite_asset_url,
        }
    )
    return env
