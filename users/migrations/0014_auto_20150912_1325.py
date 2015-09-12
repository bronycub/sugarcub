# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20150903_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='name_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
