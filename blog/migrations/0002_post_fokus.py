# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160213115339 on 2016-02-19 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fokus',
            field=models.CharField(blank='True', max_length=500, null='True'),
        ),
    ]
