# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 16:12
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
        ),
    ]
