# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:12:47 2017

@author: Administrator
"""
import  xadmin
from .models import Curve_fit,Analysis
# class Force_infoAdmin(object):
#     list_display = ['id', 'athlete','action','testid','testdate','ax','ay','az','anglex','angley','anglez']
#     search_fields = ['id', 'athlete','action','testid','testdate','ax','ay','az','anglex','angley','anglez']
#     list_filter = ['id', 'athlete','action','testid','testdate','ax','ay','az','anglex','angley','anglez']
#
# class AnalysisAdmin(object):
#     list_display = ['id', 'athlete','action','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']
#     search_fields = ['id', 'athlete','action','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']
#     list_filter = ['id', 'athlete','action','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']


# class Striking_effectAdmin(object):
#     list_display = ['id', 'athlete','action','testid','testdate','spin','speed','point']
#     search_fields = ['id', 'athlete','action','testid','testdate','spin','speed','point']
#     list_filter = ['id', 'athlete','action','testid','testdate','spin','speed','point']


class Curve_fitAdmin(object):
    list_display = ['id', 'athlete','action','testid','testdate','joint','pos_x','pos_y','pos_z','rot_x','rot_y','rot_z']
    search_fields =  ['id', 'athlete__name','action__name','testid','testdate','joint','pos_x','pos_y','pos_z','rot_x','rot_y','rot_z']
    list_filter =  ['id', 'athlete','action','testid','testdate','joint','pos_x','pos_y','pos_z','rot_x','rot_y','rot_z']
    model_icon = 'fa fa-tags'

class AnalysisAdmin(object):
    list_display = ['id', 'athlete','action','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']
    search_fields = ['id', 'athlete__name','action__name','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']
    list_filter = ['id', 'athlete','action','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']
    model_icon = 'fa fa-tags'

    data_charts = {
            "user_count": {'title': u"击球力量分析", "x-field": "id", "y-field": ('speedx','speedy','speedz','displacementx','displacementy','displacementz'), "order": ('id',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
            # "user_count2": {'title': u"生化指标-皮质醇", "x-field": "date", "y-field": ('pizhichun'), "order": ('date',)},
            # "user_count3": {'title': u"生化指标-尿素氮", "x-field": "date", "y-field": ( 'niaosudan', ), "order": ('date',)},
            # "user_count4": {'title': u"生化指标-肌酸激酶", "x-field": "date", "y-field": ( 'jisuanjimei', ), "order": ('date',)},
            # "user_count5": {'title': u"生化指标-TC", "x-field": "date", "y-field": ( 'tc'), "order": ('date',)},
    }
    
xadmin.site.register(Analysis,AnalysisAdmin)
xadmin.site.register(Curve_fit,Curve_fitAdmin)

