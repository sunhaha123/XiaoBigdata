# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:12:47 2017

@author: Administrator
"""
import  xadmin
from .models import Arrange,Hrate_info,ShenghuaDate,Performance



class ArrangeAdmin(object):
    list_display = ['id', 'athlete','timepoint','place','coach','content']
    search_fields = ['id', 'athlete','timepoint','place','coach','content']
    list_filter = ['id', 'athlete','timepoint','place','coach','content']

class Hrate_infoAdmin(object):

    list_display = ['id', 'athlete','action','testid','testdate','hr_star','hr_end','hr_min','hr_avg','hr_max']
    search_fields = ['id', 'athlete','action','testid','testdate','hr_star','hr_end','hr_min','hr_avg','hr_max']
    list_filter = ['id', 'athlete','action','testid','testdate','hr_star','hr_end','hr_min','hr_avg','hr_max']


class  ShenghuaDateAdmin(object):
    list_display = ['athlete','date','gaotong','pizhichun','niaosudan','jisuanjimei','tc','yichang']
    search_fields = ['athlete','date','gaotong','pizhichun','niaosudan','jisuanjimei','tc','yichang']
    list_filter = ['athlete','date','gaotong','pizhichun','niaosudan','jisuanjimei','tc','yichang']

class PerformanceAdmin(object):
    list_display = ['athlete','athlete','rival','date','mingcheng','xiangmu','result']
    search_fields = ['athlete','athlete','rival','date','mingcheng','xiangmu','result']
    list_filter =['athlete','athlete','rival','date','mingcheng','xiangmu','result']


xadmin.site.register(Arrange,ArrangeAdmin)
xadmin.site.register(Hrate_info,Hrate_infoAdmin)
xadmin.site.register(ShenghuaDate,ShenghuaDateAdmin)
xadmin.site.register(Performance,PerformanceAdmin)


