# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:12:47 2017

@author: Administrator
"""
import  xadmin
from .models import Motion_data,Force_order,Curve_model



# class JointAdmin(object):
#     list_display = ['jointid', 'name', 'memo', ]
#     search_fields = ['jointid', 'name', 'memo',]
#     list_filter = ['jointid', 'name', 'memo',]


class Motion_dataAdmin(object):
    list_display = ['id', 'athlete','action','testid','testdate','frameno','hip_pos_x','hip_pos_y','hip_pos_z','hip_rot_x','hip_rot_y','hip_rot_z']
    search_fields =  ['id', 'athlete__name','action__name','testid','testdate','frameno','hip_pos_x','hip_pos_y','hip_pos_z','hip_rot_x','hip_rot_y','hip_rot_z']
    list_filter =  ['id', 'athlete','action','testid','testdate','frameno','hip_pos_x','hip_pos_y','hip_pos_z','hip_rot_x','hip_rot_y','hip_rot_z']
    model_icon = 'fa fa-upload'

    data_charts = {
            "user_count": {'title': u"动作捕捉原始数据", "x-field": "testid", "y-field": ('hip_pos_x','hip_pos_y','hip_pos_z','hip_rot_x','hip_rot_y','hip_rot_z'), "order": ('testid',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
            # "user_count2": {'title': u"生化指标-皮质醇", "x-field": "date", "y-field": ('pizhichun'), "order": ('date',)},
            # "user_count3": {'title': u"生化指标-尿素氮", "x-field": "date", "y-field": ( 'niaosudan', ), "order": ('date',)},
            # "user_count4": {'title': u"生化指标-肌酸激酶", "x-field": "date", "y-field": ( 'jisuanjimei', ), "order": ('date',)},
            # "user_count5": {'title': u"生化指标-TC", "x-field": "date", "y-field": ( 'tc'), "order": ('date',)},

    }

class Force_orderAdmin(object):
    list_display = ['id', 'athlete','action','testid','testdate','Hip','LeftShoulder','LeftArm','RightShoulder','RightArm','LeftLeg','LeftFoot','RightLeg','RightFoot']
    search_fields = ['id', 'athlete__name','action__name','testid','testdate','Hip','LeftShoulder','LeftArm','RightShoulder','RightArm','LeftLeg','LeftFoot','RightLeg','RightFoot']
    list_filter = ['id', 'athlete','action','testid','testdate','Hip','LeftShoulder','LeftArm','RightShoulder','RightArm','LeftLeg','LeftFoot','RightLeg','RightFoot']
    model_icon = 'fa fa-upload'

class Curve_modelAdmin(object):
    list_display = ['id', 'action','joint','frameno','pos_x','pos_y','pos_z','rot_x','rot_y','rot_z']
    search_fields = ['id', 'action__name','joint__name','frameno','pos_x','pos_y','pos_z','rot_x','rot_y','rot_z']
    list_filter =  ['id', 'action','joint','frameno','pos_x','pos_y','pos_z','rot_x','rot_y','rot_z']
    model_icon = 'fa fa-upload'

xadmin.site.register(Motion_data,Motion_dataAdmin)
xadmin.site.register(Force_order,Force_orderAdmin)
xadmin.site.register(Curve_model,Curve_modelAdmin)
