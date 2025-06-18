from django.db import models
from django.contrib.auth.models import AbstractUser, Group as _DjangoGroup, Permission as _DjangoPermission

# Create your models here.


class User(AbstractUser):
    # username = models.EmailField(name="Email", verbose_name="Email", unique=True, max_length=255)
    # email = None

    class Meta:
        db_table = "auth_user"


class Group(_DjangoGroup):
    class Meta:
        proxy = True


class Permission(_DjangoPermission):
    class Meta:
        proxy = True
