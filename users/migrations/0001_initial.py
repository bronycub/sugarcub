# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pony',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('pony', models.CharField(max_length=32)),
                ('message', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'ponies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('bio', models.TextField()),
                ('gravatar', models.CharField(max_length=32, blank=True)),
                ('avatar', models.ImageField(upload_to='', null=True, blank=True)),
                ('phone', models.IntegerField()),
                ('birthday', models.DateField()),
                ('address', models.TextField()),
                ('addressLongitude', models.FloatField(null=True, blank=True)),
                ('addressLatitude', models.FloatField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('url', models.URLField()),
                ('icon', models.CharField(max_length=16)),
                ('profile', models.ForeignKey(to='users.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pony',
            name='profile',
            field=models.ForeignKey(to='users.Profile'),
            preserve_default=True,
        ),
    ]
