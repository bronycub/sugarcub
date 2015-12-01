# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20150515_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]
