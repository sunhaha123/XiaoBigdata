# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:12:47 2017

@author: Administrator
"""
import  xadmin
from .models import Arrange,Hrate_info,Physiology_test,Performance



class ArrangeAdmin(object):
    list_display = ['id', 'athlete','timepoint','place','coach','content']
    search_fields = ['id', 'athlete__name','timepoint','place','coach','content']
    list_filter = ['id', 'athlete','timepoint','place','coach','content']

class Hrate_infoAdmin(object):

    list_display = ['id', 'athlete','action','testid','testdate','hr_star','hr_end','hr_min','hr_avg','hr_max']
    search_fields = ['id', 'athlete__name','action__name','testid','testdate','hr_star','hr_end','hr_min','hr_avg','hr_max']
    list_filter = ['id', 'athlete','action','testid','testdate','hr_star','hr_end','hr_min','hr_avg','hr_max']


class  Physiology_testAdmin(object):
    list_display = ['athlete','date','gaotong','pizhichun','niaosudan','jisuanjimei','tc','yichang']
    search_fields = ['athlete__name','date','gaotong','pizhichun','niaosudan','jisuanjimei','tc','yichang']
    list_filter = ['athlete','date','gaotong','pizhichun','niaosudan','jisuanjimei','tc','yichang']
    model_icon = 'fa fa-tint'

    data_charts = {
            "user_count": {'title': u"生化指标-睾酮", "x-field": "date", "y-field": ("gaotong", ), "order": ('date',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
            "user_count2": {'title': u"生化指标-皮质醇", "x-field": "date", "y-field": ('pizhichun'), "order": ('date',)},
            "user_count3": {'title': u"生化指标-尿素氮", "x-field": "date", "y-field": ( 'niaosudan', ), "order": ('date',)},
            "user_count4": {'title': u"生化指标-肌酸激酶", "x-field": "date", "y-field": ( 'jisuanjimei', ), "order": ('date',)},
            "user_count5": {'title': u"生化指标-TC", "x-field": "date", "y-field": ( 'tc'), "order": ('date',)},

    }

class PerformanceAdmin(object):
    list_display = ['athlete','rival','date','mingcheng','xiangmu','result']
    search_fields = ['athlete__name','rival','date','mingcheng','xiangmu','result']
    list_filter =['athlete','rival','date','mingcheng','xiangmu','result']


xadmin.site.register(Arrange,ArrangeAdmin)
xadmin.site.register(Hrate_info,Hrate_infoAdmin)
xadmin.site.register(Physiology_test,Physiology_testAdmin)
xadmin.site.register(Performance,PerformanceAdmin)


