# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160213115339 on 2016-02-19 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160219_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategori',
            name='id_kate',
        ),
        migrations.AlterField(
            model_name='post',
            name='kategori',
            field=models.CharField(blank='False', default='umum', max_length=100, null='False'),
        ),
        migrations.DeleteModel(
            name='Kategori',
        ),
    ]
