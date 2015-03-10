# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150115_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pony',
            name='user',
        ),
        migrations.DeleteModel(
            name='Pony',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='url',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Url',
        ),
    ]
