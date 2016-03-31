# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import stdimage.models
import django.core.validators
import stdimage.utils
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('file_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Pony',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('file_name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'ponies',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
                ('name_enabled', models.BooleanField(default=True)),
                ('mail_enabled', models.BooleanField(default=True)),
                ('bio', models.TextField(validators=[django.core.validators.MinLengthValidator(150, message='The bio should be longer than 150 character')])),
                ('avatar', stdimage.models.StdImageField(blank=True, null=True, upload_to=stdimage.utils.UploadToUUID(path='avatars'))),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('phone_enabled', models.BooleanField(default=True)),
                ('birthday', models.DateField()),
                ('birthday_enabled', models.BooleanField(default=True)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=30)),
                ('postal_code', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message='The postal code must be 5 digits.', regex='^\\d[1-9]\\d{3}$')])),
                ('address_enabled', models.BooleanField(default=True)),
                ('address_longitude', models.FloatField(blank=True, null=True)),
                ('address_latitude', models.FloatField(blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPony',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('message', models.CharField(max_length=64)),
                ('pony', models.ForeignKey(to='users.Pony')),
                ('profile', models.ForeignKey(to='users.Profile')),
            ],
            options={
                'verbose_name_plural': 'ponies',
            },
        ),
        migrations.CreateModel(
            name='UserUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('url', models.URLField()),
                ('icon', models.ForeignKey(to='users.Icon')),
                ('profile', models.ForeignKey(to='users.Profile')),
            ],
        ),
    ]
