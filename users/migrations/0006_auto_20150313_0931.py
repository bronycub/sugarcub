# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150313_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gravatar',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], max_length=15),
            preserve_default=True,
        ),
    ]
