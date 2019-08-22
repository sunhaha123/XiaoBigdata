# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-08-19 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseinform', '0005_auto_20190819_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('testid', models.IntegerField(verbose_name='测试序号')),
                ('testdate', models.DateTimeField(blank=True, null=True, verbose_name='测试日期')),
                ('speedx', models.FloatField(verbose_name='线速度x')),
                ('speedy', models.FloatField(verbose_name='线速度y')),
                ('speedz', models.FloatField(verbose_name='线速度z')),
                ('displacementx', models.FloatField(verbose_name='位移x')),
                ('displacementy', models.FloatField(verbose_name='位移y')),
                ('displacementxz', models.FloatField(verbose_name='位移z')),
                ('sportworkx', models.FloatField(verbose_name='功x')),
                ('sportworky', models.FloatField(verbose_name='功y')),
                ('sportworkz', models.FloatField(verbose_name='功z')),
                ('mark', models.IntegerField(verbose_name='标识')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseinform.Action', verbose_name='击球动作')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseinform.Athlete', verbose_name='运动员')),
            ],
            options={
                'verbose_name': '击球力量数据分析',
                'verbose_name_plural': '击球力量数据分析',
            },
        ),
        migrations.AlterField(
            model_name='force_info',
            name='testid',
            field=models.IntegerField(verbose_name='测试序号'),
        ),
    ]