# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'comments', 'verbose_name': 'comment', 'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name_plural': 'events', 'verbose_name': 'event', 'ordering': ['-date_begin', '-date_end']},
        ),
        migrations.AlterModelOptions(
            name='participation',
            options={'verbose_name_plural': 'participations', 'verbose_name': 'participation', 'ordering': ['pseudo']},
        ),
        migrations.AddField(
            model_name='participation',
            name='contact',
            field=models.CharField(null=True, verbose_name='contact', max_length=31, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, verbose_name='user', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(verbose_name='event', to='agenda.Event'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pseudo',
            field=models.CharField(null=True, verbose_name='unregistered user', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(verbose_name='address', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='author',
            field=models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_begin',
            field=models.DateTimeField(verbose_name='date begin'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_end',
            field=models.DateTimeField(verbose_name='date end'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_enabled',
            field=models.CharField(verbose_name='event enabled', max_length=10, choices=[('1', 'Show both my phone and my mail'), ('2', 'Show only my mail'), ('3', 'Show only my phone')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(verbose_name='title', max_length=500),
        ),
        migrations.AlterField(
            model_name='participation',
            name='event',
            field=models.ForeignKey(verbose_name='event', to='agenda.Event'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='pseudo',
            field=models.CharField(null=True, verbose_name='unregistered user', max_length=31, blank=True),
        ),
        migrations.AlterField(
            model_name='participation',
            name='user',
            field=models.ForeignKey(null=True, verbose_name='user', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
