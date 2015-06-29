from django.contrib import admin
from .              import models


class ProfileAdmin(admin.ModelAdmin):

    def enable_profile(self, request, queryset):
        rows_updated = queryset.update(enabled = True)
        self.message_user(request, '%s profiles were enabled.', rows_updated)

    def disable_profile(self, request, queryset):
        rows_updated = queryset.update(enabled = False)
        self.message_user(request, '%s profiles were disabled.', rows_updated)

    enable_profile.short_description  = 'Enable the selected profiles.'
    disable_profile.short_description = 'Disable the selected profiles.'

    actions = [enable_profile, disable_profile]


admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Pony)
admin.site.register(models.Url)
