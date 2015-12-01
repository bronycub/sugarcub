# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20151027_1415'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pony',
            options={'verbose_name_plural': 'ponies'},
        ),
        migrations.RenameField(
            model_name='icon',
            old_name='icon_file_name',
            new_name='file_name',
        ),
        migrations.RenameField(
            model_name='icon',
            old_name='icon_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='pony',
            old_name='pony_file_name',
            new_name='file_name',
        ),
        migrations.RenameField(
            model_name='pony',
            old_name='pony_name',
            new_name='name',
        ),
    ]
