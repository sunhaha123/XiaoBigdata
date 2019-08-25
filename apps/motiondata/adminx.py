# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:12:47 2017

@author: Administrator
"""
import  xadmin
from .models import Mtion_data,Force_order



# class JointAdmin(object):
#     list_display = ['jointid', 'name', 'memo', ]
#     search_fields = ['jointid', 'name', 'memo',]
#     list_filter = ['jointid', 'name', 'memo',]


class Mtion_dataAdmin(object):
    list_display = ['id', 'athlete','action','testid','testdate','frameno','hip_pos_x','hip_pos_y','hip_pos_z','hip_rot_x','hip_rot_y','hip_rot_z']
    search_fields =  ['id', 'athlete','action','testid','testdate','frameno','hip_pos_x','hip_pos_y','hip_pos_z','hip_rot_x','hip_rot_y','hip_rot_z']
    list_filter =  ['id', 'athlete','action','testid','testdate','frameno','hip_pos_x','hip_pos_y','hip_pos_z','hip_rot_x','hip_rot_y','hip_rot_z']

class Force_orderAdmin(object):
    list_display = ['id', 'athlete','action','testid','testdate','Hip','LeftShoulder','LeftArm','RightShoulder','RightArm','LeftLeg','LeftFoot','RightLeg','RightFoot']
    search_fields = ['id', 'athlete','action','testid','testdate','Hip','LeftShoulder','LeftArm','RightShoulder','RightArm','LeftLeg','LeftFoot','RightLeg','RightFoot']
    list_filter = ['id', 'athlete','action','testid','testdate','Hip','LeftShoulder','LeftArm','RightShoulder','RightArm','LeftLeg','LeftFoot','RightLeg','RightFoot']



xadmin.site.register(Mtion_data,Mtion_dataAdmin)
xadmin.site.register(Force_order, Force_orderAdmin)

