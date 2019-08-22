# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import  AbstractUser

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u'昵称')
    birthday = models.DateField(null=True,blank=True,verbose_name=u'生日',default='2010-01-01')
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default=u"女")
    address = models.CharField(max_length=100,default=u'')
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default=u'image/default.png',max_length=100)
    # birthday = models.DateField(null=True, blank=True, verbose_name=u'生日', default='2010-01-01')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
