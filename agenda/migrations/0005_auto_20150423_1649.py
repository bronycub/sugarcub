# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20150423_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(to='agenda.Event'),
            preserve_default=True,
        ),
    ]
