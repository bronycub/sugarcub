from django.contrib              import admin
from django.contrib.auth.models  import Group
from django.contrib.sites.models import Site
from .                           import models
from django.contrib.auth.models import User
from django.contrib.auth.admin  import UserAdmin as BaseUserAdmin
from registration.models        import RegistrationProfile


class RegistrationInlines(admin.StackedInline):
    model = RegistrationProfile
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    inlines = BaseUserAdmin.inlines + [RegistrationInlines, ]


admin.site.register(models.Quote)
admin.site.register(models.Friend)

admin.site.unregister(Group)
admin.site.unregister(Site)

admin.site.unregister(RegistrationProfile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
