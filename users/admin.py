from django.contrib import admin
from django.contrib.auth.models import Group as _DjangoGroup
from django.contrib.auth.admin import UserAdmin as _DjangoUserAdmin, GroupAdmin as _DjangoGroupAdmin

from users.models import User

# Register your models here.
# admin.site.unregister(_DjangoUser)
admin.site.unregister(_DjangoGroup)


@admin.register(User)
class UserAdmin(_DjangoUserAdmin):
    pass


@admin.register(_DjangoGroup)
class GroupAdmin(_DjangoGroupAdmin):
    pass
