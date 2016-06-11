from django.contrib             import admin
from .                          import models
from django.utils.translation   import ugettext as _


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


admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Pony)
admin.site.register(models.Icon)
