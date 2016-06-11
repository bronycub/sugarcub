from django.contrib             import admin
from .                          import models
from django.utils.translation   import ugettext as _
from django.contrib.auth.models import User
from django.contrib.auth.admin  import UserAdmin as BaseUserAdmin
from registration.models        import RegistrationProfile


class PonyInline(admin.TabularInline):
    model = models.UserPony
    fk_name = 'profile'


class UrlInline(admin.TabularInline):
    model = models.UserUrl
    fk_name = 'profile'


class ProfileAdmin(admin.ModelAdmin):

    def enable_profile(self, request, queryset):
        rows_updated = queryset.update(enabled = True)
        self.message_user(request, _('%s profiles were enabled.'), rows_updated)

    def disable_profile(self, request, queryset):
        rows_updated = queryset.update(enabled = False)
        self.message_user(request, _('%s profiles were disabled.'), rows_updated)

    enable_profile.short_description  = _('Enable the selected profiles')
    disable_profile.short_description = _('Disable the selected profiles')

    actions = [enable_profile, disable_profile]
    inlines = [PonyInline, UrlInline]


class RegistrationInlines(admin.StackedInline):
    model = RegistrationProfile
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    inlines = BaseUserAdmin.inlines + [RegistrationInlines, ]


admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Pony)
admin.site.register(models.Icon)

admin.site.unregister(RegistrationProfile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
