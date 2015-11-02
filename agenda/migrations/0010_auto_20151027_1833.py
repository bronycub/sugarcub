# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0009_event_event_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_enabled',
            field=models.CharField(max_length=10, choices=[('1', 'Show both my phone and my mail'), ('2', 'Show only my mail'), ('3', 'Show only my phone')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
