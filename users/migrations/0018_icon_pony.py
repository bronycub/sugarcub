# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20151027_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('icon_name', models.CharField(max_length=32)),
                ('icon_file_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Pony',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('pony_name', models.CharField(max_length=32)),
                ('pony_file_name', models.CharField(max_length=32)),
            ],
        ),
    ]
