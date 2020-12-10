# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:12:47 2017

@author: Administrator
"""
import  xadmin
from xadmin import  views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GloabalSettings(object):
    site_title = "乒乓球训练监控大数据分析平台"
    site_footer = "中国乒乓球学院"
    menu_style = "accordion"
    model_icon = 'fa fa-tint'

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GloabalSettings)