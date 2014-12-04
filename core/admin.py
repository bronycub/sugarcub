from django.contrib import admin
from .              import models

admin.site.register(models.Profile)
admin.site.register(models.Pony)
admin.site.register(models.Url)
admin.site.register(models.Quote)
admin.site.register(models.Friend)
admin.site.register(models.Event)
