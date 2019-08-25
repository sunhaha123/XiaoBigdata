from django.db import models
from apps.baseinform.models import Athlete,Coach

# Create your models here.
class Arrange(models.Model):
    id = models.AutoField( verbose_name=u"动作ID",primary_key=True)
    # name = models.CharField(max_length=20, verbose_name=u"动作名称")
    athlete = models.ForeignKey(Athlete,verbose_name=u"运动员")
    timepoint = models.CharField(max_length=20, verbose_name=u"时间点")
    place = models.CharField(max_length=20, verbose_name=u"地点")
    coach = models.ForeignKey(Coach,verbose_name=u"教练员")
    content = models.CharField(max_length=200, verbose_name=u"训练内容")

    class Meta:
        verbose_name = u"训练计划安排"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
