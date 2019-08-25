from django.db import models
from apps.baseinform.models import  Athlete, Action
from apps.baseinform.models import Joint
# Create your models here.
class Curve_fit(models.Model):
    id = models.AutoField(verbose_name=u"ID",primary_key=True)
    athlete = models.ForeignKey(Athlete, verbose_name=u"运动员")
    action = models.ForeignKey(Action, verbose_name=u"击球动作")
    testid = models.IntegerField(verbose_name=u"测试序号")
    testdate = models.DateTimeField(verbose_name=u"测试日期",null=True,blank=True)
    joint = models.ForeignKey(Joint, verbose_name=u"关节")
    pos_x = models.FloatField(verbose_name=u'关节位移曲线相似度x')
    pos_y = models.FloatField(verbose_name=u'关节位移曲线相似度y')
    pos_z = models.FloatField(verbose_name=u'关节位移曲线相似度z')
    rot_x = models.FloatField(verbose_name=u'关节角度曲线相似x')
    rot_y = models.FloatField(verbose_name=u'关节角度曲线相似y')
    rot_z = models.FloatField(verbose_name=u'关节角度曲线相似z')

    pos_x_p1 = models.FloatField(verbose_name=u'引拍阶段位移曲线相似度x')
    pos_y_p1 = models.FloatField(verbose_name=u'引拍阶段位移曲线相似度y')
    pos_z_p1 = models.FloatField(verbose_name=u'引拍阶段位移曲线相似度z')

    pos_x_p2 = models.FloatField(verbose_name=u'挥拍击阶段位移曲线相似度x')
    pos_y_p2 = models.FloatField(verbose_name=u'挥拍击阶段位移曲线相似度y')
    pos_z_p2 = models.FloatField(verbose_name=u'挥拍击阶段位移曲线相似度z')

    pos_x_p3 = models.FloatField(verbose_name=u'还原阶段位移曲线相似度x')
    pos_y_p3 = models.FloatField(verbose_name=u'还原阶段位移曲线相似度y')
    pos_z_p3 = models.FloatField(verbose_name=u'还原阶段位移曲线相似度z')

    rot_x_p1 = models.FloatField(verbose_name=u'引拍阶段角度曲线相似度x')
    rot_y_p1 = models.FloatField(verbose_name=u'引拍阶段角度曲线相似度y')
    rot_z_p1 = models.FloatField(verbose_name=u'引拍阶段角度曲线相似度z')

    rot_x_p2 = models.FloatField(verbose_name=u'挥拍击阶段角度曲线相似度x')
    rot_y_p2 = models.FloatField(verbose_name=u'挥拍击阶段角度曲线相似度y')
    rot_z_p2 = models.FloatField(verbose_name=u'挥拍击阶段角度曲线相似度z')

    rot_x_p3 = models.FloatField(verbose_name=u'还原阶段角度曲线相似度x')
    rot_y_p3 = models.FloatField(verbose_name=u'还原阶段角度曲线相似度y')
    rot_z_p3 = models.FloatField(verbose_name=u'还原阶段角度曲线相似度z')


    class Meta:
        verbose_name = u"击球动作曲线与优秀运动员的相似度数据"
        verbose_name_plural = verbose_name

    def __int__(self):
        return self.id