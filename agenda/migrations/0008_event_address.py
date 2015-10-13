# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0007_auto_20150919_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=200, default='14 Rue basté, Bordeaux, trolololo'),
            preserve_default=False,
        ),
    ]
