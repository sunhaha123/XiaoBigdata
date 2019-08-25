from django.db import models
from apps.baseinform.models import  Athlete, Action
from apps.baseinform.models import Joint


class Striking_effect(models.Model):
    id = models.AutoField(verbose_name=u"ID", primary_key=True)
    athlete = models.ForeignKey(Athlete, verbose_name=u"运动员")
    action = models.ForeignKey(Action, verbose_name=u"击球动作")
    testid = models.IntegerField(verbose_name=u"测试序号")
    testdate = models.DateTimeField(verbose_name=u"测试日期", null=True, blank=True)
    spin = models.FloatField(verbose_name=u'转速')
    speed = models.FloatField(verbose_name=u'球速')
    point = models.IntegerField(verbose_name=u'落点',choices=((-1,"出界"),(0,"下网"),(1,"上台"),(2,"大区"),(3,"小区")))

    class Meta:
        verbose_name = u"击球质量数据"
        verbose_name_plural = verbose_name

    def __int__(self):
        return self.id


