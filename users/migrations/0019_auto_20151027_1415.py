# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_icon_pony'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpony',
            name='pony',
            field=models.ForeignKey(to='users.Pony'),
        ),
        migrations.AlterField(
            model_name='userurl',
            name='icon',
            field=models.ForeignKey(to='users.Icon'),
        ),
    ]
