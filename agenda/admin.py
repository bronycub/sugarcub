from django.contrib import admin
from .              import models

class CommentInline(admin.TabularInline):
    model = models.Comment
    fk_name = 'event'


class ParticipationInline(admin.TabularInline):
    model = models.Participation
    fk_name = 'event'


class ProfileAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ParticipationInline]


admin.site.register(models.Event, ProfileAdmin)
