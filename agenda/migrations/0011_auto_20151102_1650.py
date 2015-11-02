# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0010_auto_20151027_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='event',
            field=models.ForeignKey(to='agenda.Event'),
        ),
    ]
