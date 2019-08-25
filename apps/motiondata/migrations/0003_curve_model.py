# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-08-25 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseinform', '0008_auto_20190824_1638'),
        ('motiondata', '0002_delete_joint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curve_model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('frameno', models.IntegerField(verbose_name='帧编号')),
                ('hip_pos_x', models.FloatField(verbose_name='髋关节x轴坐标')),
                ('hip_pos_y', models.FloatField(verbose_name='髋关节y轴坐标')),
                ('hip_pos_z', models.FloatField(verbose_name='髋关节z轴坐标')),
                ('hip_rot_x', models.FloatField(verbose_name='髋关节x轴角度')),
                ('hip_rot_y', models.FloatField(verbose_name='髋关节y轴角度')),
                ('hip_rot_z', models.FloatField(verbose_name='髋关节z轴角度')),
                ('leftshoulder_pos_x', models.FloatField(verbose_name='左肩x轴坐标')),
                ('leftshoulder_pos_y', models.FloatField(verbose_name='左肩y轴坐标')),
                ('leftshoulder_pos_z', models.FloatField(verbose_name='左肩z轴坐标')),
                ('leftshoulder_rot_x', models.FloatField(verbose_name='左肩x轴角度')),
                ('leftshoulder_rot_y', models.FloatField(verbose_name='左肩y轴角度')),
                ('leftshoulder_rot_z', models.FloatField(verbose_name='左肩z轴角度')),
                ('leftarm_pos_x', models.FloatField(verbose_name='左肘x轴角度')),
                ('leftarm_pos_y', models.FloatField(verbose_name='左肘y轴角度')),
                ('leftarm_pos_z', models.FloatField(verbose_name='左肘z轴角度')),
                ('rightshoulder_pos_x', models.FloatField(verbose_name='右肩x轴坐标')),
                ('rightshoulder_pos_y', models.FloatField(verbose_name='右肩y轴坐标')),
                ('rightshoulder_pos_z', models.FloatField(verbose_name='右肩z轴坐标')),
                ('rightshoulder_rot_x', models.FloatField(verbose_name='右肩x轴角度')),
                ('rightshoulder_rot_y', models.FloatField(verbose_name='右肩y轴角度')),
                ('rightshoulder_rot_z', models.FloatField(verbose_name='右肩z轴角度')),
                ('rightarm_pos_x', models.FloatField(verbose_name='右肘x轴坐标')),
                ('rightarm_pos_y', models.FloatField(verbose_name='右肘y轴坐标')),
                ('rightarm_pos_z', models.FloatField(verbose_name='右肘z轴坐标')),
                ('rightarm_rot_x', models.FloatField(verbose_name='右肘x轴角度')),
                ('rightarm_rot_y', models.FloatField(verbose_name='右肘y轴角度')),
                ('rightarm_rot_z', models.FloatField(verbose_name='右肘z轴角度')),
                ('leftleg_pos_x', models.FloatField(verbose_name='左膝x轴坐标')),
                ('leftleg_pos_y', models.FloatField(verbose_name='左膝y轴坐标')),
                ('leftleg_pos_z', models.FloatField(verbose_name='左膝z轴坐标')),
                ('leftleg_rot_y', models.FloatField(verbose_name='左膝y轴角度')),
                ('leftleg_rot_z', models.FloatField(verbose_name='左膝z轴角度')),
                ('leftfoot_pos_x', models.FloatField(verbose_name='左踝x轴坐标')),
                ('leftfoot_pos_y', models.FloatField(verbose_name='左踝y轴坐标')),
                ('leftfoot_pos_z', models.FloatField(verbose_name='左踝z轴坐标')),
                ('leftfoot_rot_x', models.FloatField(verbose_name='左踝x轴角度')),
                ('leftfoot_rot_y', models.FloatField(verbose_name='左踝y轴角度')),
                ('leftfoot_rot_z', models.FloatField(verbose_name='左踝z轴角度')),
                ('rightleg_pos_x', models.FloatField(verbose_name='右膝x轴坐标')),
                ('rightleg_pos_y', models.FloatField(verbose_name='右膝y轴坐标')),
                ('rightleg_pos_z', models.FloatField(verbose_name='右膝z轴坐标')),
                ('rightleg_rot_x', models.FloatField(verbose_name='右膝x轴角度')),
                ('rightleg_rot_y', models.FloatField(verbose_name='右膝y轴角度')),
                ('rightleg_rot_z', models.FloatField(verbose_name='右膝z轴角度')),
                ('rightfoot_pos_x', models.FloatField(verbose_name='右踝x轴坐标')),
                ('rightfoot_pos_y', models.FloatField(verbose_name='右踝y轴坐标')),
                ('rightfoot_pos_z', models.FloatField(verbose_name='右踝z轴坐标')),
                ('rightfoot_rot_x', models.FloatField(verbose_name='右踝x轴角度')),
                ('rightfoot_rot_y', models.FloatField(verbose_name='右踝y轴角度')),
                ('rightfoot_rot_z', models.FloatField(verbose_name='右踝z轴角度')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseinform.Action', verbose_name='击球动作')),
            ],
            options={
                'verbose_name': '击球动作曲线模型',
                'verbose_name_plural': '击球动作曲线模型',
            },
        ),
    ]