# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0014_auto_20160202_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='contact',
            field=models.CharField(null=True, blank=True, max_length=31),
        ),
    ]
