# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-08-24 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseinform', '0007_auto_20190819_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joint',
            fields=[
                ('jointid', models.IntegerField(primary_key=True, serialize=False, verbose_name='关节ID')),
                ('name', models.CharField(max_length=20, verbose_name='关节名称')),
                ('memo', models.CharField(max_length=20, verbose_name='备忘录')),
            ],
            options={
                'verbose_name_plural': '人体主要关节',
                'verbose_name': '人体主要关节',
            },
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='action',
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='athlete',
        ),
        migrations.RemoveField(
            model_name='arrange',
            name='athlete',
        ),
        migrations.RemoveField(
            model_name='arrange',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='force_info',
            name='action',
        ),
        migrations.RemoveField(
            model_name='force_info',
            name='athlete',
        ),
        migrations.DeleteModel(
            name='Analysis',
        ),
        migrations.DeleteModel(
            name='Arrange',
        ),
        migrations.DeleteModel(
            name='Force_info',
        ),
    ]
