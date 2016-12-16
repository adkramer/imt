# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='unitgroup',
        ),
        migrations.AddField(
            model_name='unitgroup',
            name='unit',
            field=models.ManyToManyField(to='items.Unit'),
        ),
    ]
