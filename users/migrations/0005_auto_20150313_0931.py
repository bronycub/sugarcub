# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150213_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
