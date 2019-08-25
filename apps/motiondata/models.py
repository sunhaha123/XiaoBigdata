from __future__ import unicode_literals
from  datetime import datetime
from django.db import models
from apps.baseinform.models import  Athlete, Action




class Mtion_data(models.Model):
    id = models.AutoField(verbose_name=u"ID",primary_key=True)
    athlete = models.ForeignKey(Athlete, verbose_name=u"运动员")
    action = models.ForeignKey(Action, verbose_name=u"击球动作")
    testid = models.IntegerField(verbose_name=u"测试序号")
    testdate = models.DateTimeField(verbose_name=u"测试日期",null=True,blank=True)
    frameno = models.IntegerField(verbose_name=u"帧编号")

    hip_pos_x = models.FloatField(verbose_name=u'髋关节x轴坐标')
    hip_pos_y = models.FloatField(verbose_name=u'髋关节y轴坐标')
    hip_pos_z = models.FloatField(verbose_name=u'髋关节z轴坐标')
    hip_rot_x = models.FloatField(verbose_name=u'髋关节x轴角度')
    hip_rot_y = models.FloatField(verbose_name=u'髋关节y轴角度')
    hip_rot_z = models.FloatField(verbose_name=u'髋关节z轴角度')

    leftshoulder_pos_x = models.FloatField(verbose_name=u'左肩x轴坐标')
    leftshoulder_pos_y = models.FloatField(verbose_name=u'左肩y轴坐标')
    leftshoulder_pos_z = models.FloatField(verbose_name=u'左肩z轴坐标')
    leftshoulder_rot_x = models.FloatField(verbose_name=u'左肩x轴角度')
    leftshoulder_rot_y = models.FloatField(verbose_name=u'左肩y轴角度')
    leftshoulder_rot_z = models.FloatField(verbose_name=u'左肩z轴角度')

    leftarm_pos_x = models.FloatField(verbose_name=u'左肘x轴坐标')
    leftarm_pos_y = models.FloatField(verbose_name=u'左肘y轴坐标')
    leftarm_pos_z = models.FloatField(verbose_name=u'左肘z轴坐标')
    leftarm_pos_x = models.FloatField(verbose_name=u'左肘x轴角度')
    leftarm_pos_y = models.FloatField(verbose_name=u'左肘y轴角度')
    leftarm_pos_z = models.FloatField(verbose_name=u'左肘z轴角度')

    rightshoulder_pos_x = models.FloatField(verbose_name=u'右肩x轴坐标')
    rightshoulder_pos_y = models.FloatField(verbose_name=u'右肩y轴坐标')
    rightshoulder_pos_z = models.FloatField(verbose_name=u'右肩z轴坐标')
    rightshoulder_rot_x = models.FloatField(verbose_name=u'右肩x轴角度')
    rightshoulder_rot_y = models.FloatField(verbose_name=u'右肩y轴角度')
    rightshoulder_rot_z = models.FloatField(verbose_name=u'右肩z轴角度')

    rightarm_pos_x = models.FloatField(verbose_name=u'右肘x轴坐标')
    rightarm_pos_y = models.FloatField(verbose_name=u'右肘y轴坐标')
    rightarm_pos_z = models.FloatField(verbose_name=u'右肘z轴坐标')
    rightarm_rot_x = models.FloatField(verbose_name=u'右肘x轴角度')
    rightarm_rot_y =  models.FloatField(verbose_name=u'右肘y轴角度')
    rightarm_rot_z = models.FloatField(verbose_name=u'右肘z轴角度')

    leftleg_pos_x = models.FloatField(verbose_name=u'左膝x轴坐标')
    leftleg_pos_y = models.FloatField(verbose_name=u'左膝y轴坐标')
    leftleg_pos_z = models.FloatField(verbose_name=u'左膝z轴坐标')
    leftleg_rot_y = models.FloatField(verbose_name=u'左膝x轴角度')
    leftleg_rot_y = models.FloatField(verbose_name=u'左膝y轴角度')
    leftleg_rot_z = models.FloatField(verbose_name=u'左膝z轴角度')

    leftfoot_pos_x = models.FloatField(verbose_name=u'左踝x轴坐标')
    leftfoot_pos_y = models.FloatField(verbose_name=u'左踝y轴坐标')
    leftfoot_pos_z = models.FloatField(verbose_name=u'左踝z轴坐标')
    leftfoot_rot_x = models.FloatField(verbose_name=u'左踝x轴角度')
    leftfoot_rot_y = models.FloatField(verbose_name=u'左踝y轴角度')
    leftfoot_rot_z = models.FloatField(verbose_name=u'左踝z轴角度')

    rightleg_pos_x = models.FloatField(verbose_name=u'右膝x轴坐标')
    rightleg_pos_y = models.FloatField(verbose_name=u'右膝y轴坐标')
    rightleg_pos_z = models.FloatField(verbose_name=u'右膝z轴坐标')
    rightleg_rot_x = models.FloatField(verbose_name=u'右膝x轴角度')
    rightleg_rot_y = models.FloatField(verbose_name=u'右膝y轴角度')
    rightleg_rot_z = models.FloatField(verbose_name=u'右膝z轴角度')

    rightfoot_pos_x = models.FloatField(verbose_name=u'右踝x轴坐标')
    rightfoot_pos_y = models.FloatField(verbose_name=u'右踝y轴坐标')
    rightfoot_pos_z = models.FloatField(verbose_name=u'右踝z轴坐标')
    rightfoot_rot_x = models.FloatField(verbose_name=u'右踝x轴角度')
    rightfoot_rot_y = models.FloatField(verbose_name=u'右踝y轴角度')
    rightfoot_rot_z = models.FloatField(verbose_name=u'右踝z轴角度')


    class Meta:
        verbose_name = u"动作捕捉原始数据"
        verbose_name_plural = verbose_name

    def __int__(self):
        return self.id


class Force_order(models.Model):
    id = models.AutoField(verbose_name=u"ID",primary_key=True)
    athlete = models.ForeignKey(Athlete, verbose_name=u"运动员")
    action = models.ForeignKey(Action, verbose_name=u"击球动作")
    testid = models.IntegerField(verbose_name=u"测试序号")
    testdate = models.DateTimeField(verbose_name=u"测试日期",null=True,blank=True)
    Hip = models.IntegerField(verbose_name=u'髋关节')
    LeftShoulder = models.IntegerField(verbose_name=u'左肩关节')
    LeftArm = models.IntegerField(verbose_name=u'左肘关节')
    RightShoulder = models.IntegerField(verbose_name=u'右肩关节')
    RightArm = models.IntegerField(verbose_name=u'右肘关节')
    LeftLeg = models.IntegerField(verbose_name=u'左膝关节')
    LeftFoot = models.IntegerField(verbose_name=u'左踝关节')
    RightLeg = models.IntegerField(verbose_name=u'右膝关节')
    RightFoot = models.IntegerField(verbose_name=u'右踝关节')



    class Meta:
        verbose_name = u"关节点发力顺序数据"
        verbose_name_plural = verbose_name

    def __int__(self):
        return self.id


class Curve_model(models.Model):
    id = models.AutoField(verbose_name=u"ID",primary_key=True)
    # athlete = models.ForeignKey(Athlete, verbose_name=u"运动员")
    action = models.ForeignKey(Action, verbose_name=u"击球动作")
    # testid = models.IntegerField(verbose_name=u"测试序号")
    # testdate = models.DateTimeField(verbose_name=u"测试日期",null=True,blank=True)
    frameno = models.IntegerField(verbose_name=u"帧编号")

    hip_pos_x = models.FloatField(verbose_name=u'髋关节x轴坐标')
    hip_pos_y = models.FloatField(verbose_name=u'髋关节y轴坐标')
    hip_pos_z = models.FloatField(verbose_name=u'髋关节z轴坐标')
    hip_rot_x = models.FloatField(verbose_name=u'髋关节x轴角度')
    hip_rot_y = models.FloatField(verbose_name=u'髋关节y轴角度')
    hip_rot_z = models.FloatField(verbose_name=u'髋关节z轴角度')

    leftshoulder_pos_x = models.FloatField(verbose_name=u'左肩x轴坐标')
    leftshoulder_pos_y = models.FloatField(verbose_name=u'左肩y轴坐标')
    leftshoulder_pos_z = models.FloatField(verbose_name=u'左肩z轴坐标')
    leftshoulder_rot_x = models.FloatField(verbose_name=u'左肩x轴角度')
    leftshoulder_rot_y = models.FloatField(verbose_name=u'左肩y轴角度')
    leftshoulder_rot_z = models.FloatField(verbose_name=u'左肩z轴角度')

    leftarm_pos_x = models.FloatField(verbose_name=u'左肘x轴坐标')
    leftarm_pos_y = models.FloatField(verbose_name=u'左肘y轴坐标')
    leftarm_pos_z = models.FloatField(verbose_name=u'左肘z轴坐标')
    leftarm_pos_x = models.FloatField(verbose_name=u'左肘x轴角度')
    leftarm_pos_y = models.FloatField(verbose_name=u'左肘y轴角度')
    leftarm_pos_z = models.FloatField(verbose_name=u'左肘z轴角度')

    rightshoulder_pos_x = models.FloatField(verbose_name=u'右肩x轴坐标')
    rightshoulder_pos_y = models.FloatField(verbose_name=u'右肩y轴坐标')
    rightshoulder_pos_z = models.FloatField(verbose_name=u'右肩z轴坐标')
    rightshoulder_rot_x = models.FloatField(verbose_name=u'右肩x轴角度')
    rightshoulder_rot_y = models.FloatField(verbose_name=u'右肩y轴角度')
    rightshoulder_rot_z = models.FloatField(verbose_name=u'右肩z轴角度')

    rightarm_pos_x = models.FloatField(verbose_name=u'右肘x轴坐标')
    rightarm_pos_y = models.FloatField(verbose_name=u'右肘y轴坐标')
    rightarm_pos_z = models.FloatField(verbose_name=u'右肘z轴坐标')
    rightarm_rot_x = models.FloatField(verbose_name=u'右肘x轴角度')
    rightarm_rot_y =  models.FloatField(verbose_name=u'右肘y轴角度')
    rightarm_rot_z = models.FloatField(verbose_name=u'右肘z轴角度')

    leftleg_pos_x = models.FloatField(verbose_name=u'左膝x轴坐标')
    leftleg_pos_y = models.FloatField(verbose_name=u'左膝y轴坐标')
    leftleg_pos_z = models.FloatField(verbose_name=u'左膝z轴坐标')
    leftleg_rot_y = models.FloatField(verbose_name=u'左膝x轴角度')
    leftleg_rot_y = models.FloatField(verbose_name=u'左膝y轴角度')
    leftleg_rot_z = models.FloatField(verbose_name=u'左膝z轴角度')

    leftfoot_pos_x = models.FloatField(verbose_name=u'左踝x轴坐标')
    leftfoot_pos_y = models.FloatField(verbose_name=u'左踝y轴坐标')
    leftfoot_pos_z = models.FloatField(verbose_name=u'左踝z轴坐标')
    leftfoot_rot_x = models.FloatField(verbose_name=u'左踝x轴角度')
    leftfoot_rot_y = models.FloatField(verbose_name=u'左踝y轴角度')
    leftfoot_rot_z = models.FloatField(verbose_name=u'左踝z轴角度')

    rightleg_pos_x = models.FloatField(verbose_name=u'右膝x轴坐标')
    rightleg_pos_y = models.FloatField(verbose_name=u'右膝y轴坐标')
    rightleg_pos_z = models.FloatField(verbose_name=u'右膝z轴坐标')
    rightleg_rot_x = models.FloatField(verbose_name=u'右膝x轴角度')
    rightleg_rot_y = models.FloatField(verbose_name=u'右膝y轴角度')
    rightleg_rot_z = models.FloatField(verbose_name=u'右膝z轴角度')

    rightfoot_pos_x = models.FloatField(verbose_name=u'右踝x轴坐标')
    rightfoot_pos_y = models.FloatField(verbose_name=u'右踝y轴坐标')
    rightfoot_pos_z = models.FloatField(verbose_name=u'右踝z轴坐标')
    rightfoot_rot_x = models.FloatField(verbose_name=u'右踝x轴角度')
    rightfoot_rot_y = models.FloatField(verbose_name=u'右踝y轴角度')
    rightfoot_rot_z = models.FloatField(verbose_name=u'右踝z轴角度')


    class Meta:
        verbose_name = u"击球动作曲线模型"
        verbose_name_plural = verbose_name

    def __int__(self):
        return self.id
