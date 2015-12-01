# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPony',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('pony', models.CharField(max_length=32)),
                ('message', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'ponies',
            },
        ),
        migrations.CreateModel(
            name='UserUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('url', models.URLField()),
                ('icon', models.CharField(max_length=16)),
            ],
        ),
        migrations.RemoveField(
            model_name='pony',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='url',
            name='profile',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], max_length=15),
        ),
        migrations.DeleteModel(
            name='Pony',
        ),
        migrations.DeleteModel(
            name='Url',
        ),
        migrations.AddField(
            model_name='userurl',
            name='profile',
            field=models.ForeignKey(to='users.Profile'),
        ),
        migrations.AddField(
            model_name='userpony',
            name='profile',
            field=models.ForeignKey(to='users.Profile'),
        ),
    ]
