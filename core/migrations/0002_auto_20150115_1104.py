# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='addressLontatidue',
        ),
        migrations.AddField(
            model_name='friend',
            name='image',
            field=models.ImageField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='addressLatitude',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='addressLongitude',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(verbose_name='bio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='gravatar',
            field=models.CharField(blank=True, verbose_name='gravatar', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(verbose_name='téléphone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
