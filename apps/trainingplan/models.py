from django.db import models
from apps.baseinform.models import Athlete,Coach,Action

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


class Hrate_info(models.Model):
    id = models.AutoField( verbose_name=u"ID",primary_key=True)
    # name = models.CharField(max_length=20, verbose_name=u"动作名称")
    athlete = models.ForeignKey(Athlete,verbose_name=u"运动员")
    action = models.ForeignKey(Action, verbose_name=u"动作")
    testid = models.IntegerField(verbose_name=u"测试序号")
    testdate = models.DateTimeField(null=True,blank=True, verbose_name=u"训练日期")
    hr_star = models.FloatField(verbose_name=u'训练开始心率')
    hr_end = models.FloatField(verbose_name=u'训练结束心率')
    hr_min = models.FloatField(verbose_name=u'心率最小值')
    hr_avg = models.FloatField(verbose_name=u'心率平均值')
    hr_max = models.FloatField(verbose_name=u'心率最大值')

    class Meta:
        verbose_name = u"训练强度"
        verbose_name_plural = verbose_name

    def __int__(self):
        return self.id


class Physiology_test(models.Model):
    id = models.AutoField(verbose_name=u"ID",primary_key=True)
    athlete = models.ForeignKey(Athlete, verbose_name=u'运动员姓名')
    date = models.DateField(null=True, blank=True, verbose_name=u'检验日期')
    gaotong = models.FloatField(verbose_name=u'睾酮')
    pizhichun = models.FloatField(verbose_name=u'皮质醇')
    niaosudan = models.FloatField(verbose_name=u'尿素氮')
    tc = models.FloatField(verbose_name=u'总胆固醇')
    jisuanjimei = models.FloatField(verbose_name=u'肌酸激酶')
    yichang = models.CharField(max_length=50,  null=True, blank=True, verbose_name=u'异常数据说明')


    class Meta:
        verbose_name = u'生化指标'
        verbose_name_plural = verbose_name

    def __int__(self):
        return self.id



class Performance(models.Model):
    id = models.AutoField(verbose_name=u"ID",primary_key=True)
    athlete = models.ForeignKey(Athlete, verbose_name=u'运动员姓名')
    rival= models.CharField(max_length=50,null=True, blank=True, verbose_name=u'对手名称')
    date = models.DateField(null=True, blank=True, verbose_name=u'比赛日期')
    mingcheng = models.CharField(max_length=50,null=True, blank=True, verbose_name=u'比赛名称')
    xiangmu = models.IntegerField(verbose_name=u"项目",choices=((1,"单打"),(2,"双打")))
    result = models.CharField(max_length=50,verbose_name=u'比赛结果：总比分')
    r1 = models.CharField(max_length=50,verbose_name=u'第1局比分')
    r2 = models.CharField(max_length=50,verbose_name=u'第2局比分')
    r3 = models.CharField(max_length=50,verbose_name=u'第3局比分')
    r4 = models.CharField(max_length=50,verbose_name=u'第4局比分')
    r5 = models.CharField(max_length=50,verbose_name=u'第5局比分')
    r6 = models.CharField(max_length=50,verbose_name=u'第6局比分')
    r7 = models.CharField(max_length=50,verbose_name=u'第7局比分')

    class Meta:
        verbose_name = u'比赛成绩'
        verbose_name_plural = verbose_name

    def __int__(self):
        return self.id