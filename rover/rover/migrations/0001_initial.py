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
            name='Dog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(choices=[(1, 'Owner'), (2, 'Sitter'), (3, 'Both')])),
                ('image', models.URLField(null=True)),
                ('text', models.TextField(null=True)),
                ('rank', models.FloatField(null=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('dogs', models.ManyToManyField(to='rover.Dog')),
                ('sitter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
