# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20150912_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mail_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
