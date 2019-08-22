# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:12:47 2017

@author: Administrator
"""
import  xadmin
from .models import Coach,Athlete,Action,Arrange,Force_info,Analysis

class AthleteAdmin(object):
    list_display = [ 'athleteid','name', 'sfzh','csrq','gender','height','weight','years','grade','coach']
    search_fields = [  'athleteid','name', 'sfzh','csrq','gender','height','weight','years','grade','coach']
    list_filter = [  'athleteid','name', 'sfzh','csrq','gender','height','weight','years','grade','coach']


class CoachAdmin(object):
    list_display = [ 'coachid','name', 'gender', 'grade','years']
    search_fields = [ 'coachid','name', 'gender', 'grade','years']
    list_filter = [ 'coachid','name', 'gender', 'grade','years']


class ActionAdmin(object):
    list_display = ['actionid', 'name', 'memo', ]
    search_fields = ['actionid', 'name', 'memo',]
    list_filter = ['actionid', 'name', 'memo',]


class ArrangeAdmin(object):
    list_display = ['id', 'athlete','timepoint','place','coach','content']
    search_fields = ['id', 'athlete','timepoint','place','coach','content']
    list_filter = ['id', 'athlete','timepoint','place','coach','content']


class Force_infoAdmin(object):
    list_display = ['id', 'athlete','action','testid','testdate','ax','ay','az','anglex','angley','anglez']
    search_fields = ['id', 'athlete','action','testid','testdate','ax','ay','az','anglex','angley','anglez']
    list_filter = ['id', 'athlete','action','testid','testdate','ax','ay','az','anglex','angley','anglez']

class AnalysisAdmin(object):
    list_display = ['id', 'athlete','action','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']
    search_fields = ['id', 'athlete','action','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']
    list_filter = ['id', 'athlete','action','testid','testdate','speedx','speedy','speedz','displacementx','displacementy','displacementz']


xadmin.site.register(Coach, CoachAdmin)
xadmin.site.register(Athlete, AthleteAdmin)
xadmin.site.register(Action, ActionAdmin)
xadmin.site.register(Arrange, ArrangeAdmin)
xadmin.site.register(Force_info, Force_infoAdmin)
xadmin.site.register(Analysis, AnalysisAdmin)
