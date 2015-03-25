# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
    ]
