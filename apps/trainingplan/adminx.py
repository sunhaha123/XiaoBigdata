# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:12:47 2017

@author: Administrator
"""
import  xadmin
from .models import Arrange



class ArrangeAdmin(object):
    list_display = ['id', 'athlete','timepoint','place','coach','content']
    search_fields = ['id', 'athlete','timepoint','place','coach','content']
    list_filter = ['id', 'athlete','timepoint','place','coach','content']

xadmin.site.register(Arrange,ArrangeAdmin)

