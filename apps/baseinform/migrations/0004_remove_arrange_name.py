# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-08-19 20:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseinform', '0003_auto_20190819_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrange',
            name='name',
        ),
    ]
