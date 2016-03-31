# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('pseudo', models.CharField(blank=True, null=True, max_length=30)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date_begin', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('address', models.CharField(max_length=200)),
                ('event_enabled', models.CharField(choices=[('1', 'Show both my phone and my mail'), ('2', 'Show only my mail'), ('3', 'Show only my phone')], max_length=10)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_begin', '-date_end'],
            },
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('pseudo', models.CharField(blank=True, null=True, max_length=31)),
                ('event', models.ForeignKey(to='agenda.Event')),
                ('user', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(to='agenda.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set([('pseudo', 'event'), ('user', 'event')]),
        ),
    ]
