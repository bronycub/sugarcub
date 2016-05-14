from django.contrib import admin
from .              import models


class CommentInline(admin.TabularInline):
    model = models.Comment
    fk_name = 'event'


class ParticipationInline(admin.TabularInline):
    model = models.Participation
    fk_name = 'event'


class EventAdmin(admin.ModelAdmin):
    inlines = [ParticipationInline, CommentInline]


admin.site.register(models.Event, EventAdmin)
