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


class AnalysisAdmin(object):
    list_display = ['id', 'athlete','action','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']
    search_fields = ['id', 'athlete__name','action__name','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']
    list_filter = ['id', 'athlete','action','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']

xadmin.site.register(Analysis,AnalysisAdmin)
xadmin.site.register(Curve_fit,Curve_fitAdmin)

