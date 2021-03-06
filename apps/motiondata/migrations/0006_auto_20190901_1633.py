# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-09-01 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motiondata', '0005_auto_20190901_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curve_model',
            name='pos_x',
            field=models.FloatField(blank=True, null=True, verbose_name='关节x方向坐标'),
        ),
        migrations.AlterField(
            model_name='curve_model',
            name='pos_y',
            field=models.FloatField(blank=True, null=True, verbose_name='关节y方向坐标'),
        ),
        migrations.AlterField(
            model_name='curve_model',
            name='pos_z',
            field=models.FloatField(blank=True, null=True, verbose_name='关节z方向坐标'),
        ),
        migrations.AlterField(
            model_name='curve_model',
            name='rot_x',
            field=models.FloatField(blank=True, null=True, verbose_name='关节z方向角度'),
        ),
        migrations.AlterField(
            model_name='curve_model',
            name='rot_y',
            field=models.FloatField(blank=True, null=True, verbose_name='关节z方向角度'),
        ),
        migrations.AlterField(
            model_name='curve_model',
            name='rot_z',
            field=models.FloatField(blank=True, null=True, verbose_name='关节z方向角度'),
        ),
    ]
