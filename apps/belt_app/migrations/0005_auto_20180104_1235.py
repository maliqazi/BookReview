# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-04 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0004_auto_20180104_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='user',
            field=models.ManyToManyField(related_name='reviews', to='belt_app.Users'),
        ),
    ]
