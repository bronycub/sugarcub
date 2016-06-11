from django.contrib              import admin
from django.contrib.auth.models  import Group
from django.contrib.sites.models import Site
from .                           import models


admin.site.register(models.Quote)
admin.site.register(models.Friend)

admin.site.unregister(Group)
admin.site.unregister(Site)
