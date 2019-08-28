from __future__ import unicode_literals
from  datetime import datetime
from django.db import models


class Coach(models.Model):
    coachid = models.IntegerField(verbose_name=u"教练员ID",primary_key=True)
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default=u"女")
    address = models.CharField(max_length=200, verbose_name=u"居住地",null=True,blank=True)
    grade = models.CharField(max_length=200, verbose_name=u"教练员等级",null=True,blank=True)
    years = models.IntegerField(verbose_name=u"执教年数")
    team_name = models.CharField(max_length=50, verbose_name=u"所在运动队名称",null=True,blank=True)

    class Meta:
        verbose_name = u"教练员"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Athlete(models.Model):
    athleteid = models.IntegerField(verbose_name=u"运动员ID",primary_key=True)
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    sfzh = models.CharField(max_length=20, verbose_name=u"身份证号")
    csrq = models.DateTimeField(null=True,blank=True, verbose_name=u"出生日期")
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default=u"女")
    height = models.DecimalField( max_digits=8, decimal_places=2,)
    weight = models.DecimalField( max_digits=8, decimal_places=2,)
    birthplace = models.CharField(max_length=200, verbose_name=u"出生地",null=True,blank=True)
    address = models.CharField(max_length=200, verbose_name=u"居住地",null=True,blank=True)
    grade = models.CharField(max_length=200, verbose_name=u"运动员等级",null=True,blank=True)
    years = models.IntegerField(verbose_name=u"运动年限")
    dflx = models.CharField(max_length=200, verbose_name=u"打法类型",null=True,blank=True)
    bscj = models.CharField(max_length=200, verbose_name=u"比赛成绩",null=True,blank=True)
    coach = models.ForeignKey(Coach,verbose_name=u"教练员")
    entrance_date =  models.CharField(max_length=20, verbose_name=u"入队年份",null=True,blank=True)
    retired = models.CharField(max_length=5, verbose_name=u"是否离队",choices=(("true","已经离队"),("false","未离队")),default="false")

    class Meta:
        verbose_name = u"运动员"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Action(models.Model):
    actionid = models.IntegerField(verbose_name=u"动作ID",primary_key=True)
    name = models.CharField(max_length=20, verbose_name=u"动作名称")
    memo = models.CharField(max_length=20, verbose_name=u"备忘录")

    class Meta:
        verbose_name = u"击球动作"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Joint(models.Model):
    jointid = models.IntegerField(verbose_name=u"关节ID",primary_key=True)
    name = models.CharField(max_length=20, verbose_name=u"关节名称")
    memo = models.CharField(max_length=20, verbose_name=u"备忘录")

    class Meta:
        verbose_name = u"人体主要关节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



# class Arrange(models.Model):
#     id = models.AutoField( verbose_name=u"动作ID",primary_key=True)
#     # name = models.CharField(max_length=20, verbose_name=u"动作名称")
#     athlete = models.ForeignKey(Athlete,verbose_name=u"运动员")
#     timepoint = models.CharField(max_length=20, verbose_name=u"时间点")
#     place = models.CharField(max_length=20, verbose_name=u"地点")
#     coach = models.ForeignKey(Coach,verbose_name=u"教练员")
#     content = models.CharField(max_length=200, verbose_name=u"训练内容")
#
#     class Meta:
#         verbose_name = u"训练计划安排"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.content
#
#
# class Force_info(models.Model):
#     id = models.AutoField(verbose_name=u"ID",primary_key=True)
#     athlete = models.ForeignKey(Athlete, verbose_name=u"运动员")
#     action = models.ForeignKey(Action, verbose_name=u"击球动作")
#     testid = models.IntegerField(verbose_name=u"测试序号")
#     testdate = models.DateTimeField(verbose_name=u"测试日期",null=True,blank=True)
#     ax = models.FloatField(verbose_name=u'线加速度x')
#     ay = models.FloatField(verbose_name=u'线加速度y')
#     az = models.FloatField(verbose_name=u'线加速度z')
#     anglex = models.FloatField(verbose_name=u'角加速度x')
#     angley = models.FloatField(verbose_name=u'角加速度y')
#     anglez = models.FloatField(verbose_name=u'角加速度z')
#     avx = models.FloatField(verbose_name=u'线速度x')
#     avy = models.FloatField(verbose_name=u'线速度y')
#     avz = models.FloatField(verbose_name=u'线速度z')
#     magnetismx = models.FloatField(verbose_name=u'地磁x')
#     magnetismy = models.FloatField(verbose_name=u'地磁y')
#     magnetismz = models.FloatField(verbose_name=u'地磁z')
#     temperature= models.FloatField(verbose_name=u'温度')
#     mark =  models.IntegerField(verbose_name=u'标识')
#
#     class Meta:
#         verbose_name = u"击球力量原始数据"
#         verbose_name_plural = verbose_name
#
#     def __int__(self):
#         return self.id
#
#
# class Analysis(models.Model):
#     id = models.AutoField(verbose_name=u"ID",primary_key=True)
#     athlete = models.ForeignKey(Athlete, verbose_name=u"运动员")
#     action = models.ForeignKey(Action, verbose_name=u"击球动作")
#     testid = models.IntegerField(verbose_name=u"测试序号")
#     testdate = models.DateTimeField(verbose_name=u"测试日期",null=True,blank=True)
#     speedx = models.FloatField(verbose_name=u'线速度x')
#     speedy = models.FloatField(verbose_name=u'线速度y')
#     speedz = models.FloatField(verbose_name=u'线速度z')
#     displacementx = models.FloatField(verbose_name=u'位移x')
#     displacementy = models.FloatField(verbose_name=u'位移y')
#     displacementz = models.FloatField(verbose_name=u'位移z')
#     sportworkx = models.FloatField(verbose_name=u'功x')
#     sportworky = models.FloatField(verbose_name=u'功y')
#     sportworkz = models.FloatField(verbose_name=u'功z')
#     mark =  models.IntegerField(verbose_name=u'标识')
#
#     class Meta:
#         verbose_name = u"击球力量数据分析"
#         verbose_name_plural = verbose_name
#
#     def __int__(self):
#         return self.id


