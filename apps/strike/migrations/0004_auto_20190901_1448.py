# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-09-01 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strike', '0003_auto_20190825_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='force_info',
            name='a',
            field=models.FloatField(default=1, verbose_name='三个方向的合加速度'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='force_info',
            name='f',
            field=models.FloatField(default=1, verbose_name='合力'),
            preserve_default=False,
        ),
    ]
