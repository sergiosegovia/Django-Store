# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20161106_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_create',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='date_update',
            field=models.DateField(auto_now=True),
        ),
    ]
