# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-27 11:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('frecuenciaconsumo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidad',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 3, 27, 11, 52, 48, 494693, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unidad',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 3, 27, 11, 53, 24, 31267, tzinfo=utc)),
            preserve_default=False,
        ),
    ]