# -*- coding:utf-8 -*-
import xadmin
from xadmin import views

from models import AboutUs, HonorInfo, Honors


class HonorsInline(object):
    model = Honors
    extra = 0


class HonorInfoAdmin(object):
    list_display = ['title', 'order', 'create_time']
    search_fields = ['title']
    list_filter = ['order', 'create_time']
    list_editable = ['order']
    inlines = [HonorsInline]
    model_icon = 'fa fa-font-awesome'


class AboutUsAdmin(object):
    list_display = ['title', 'order', 'create_time']
    search_fields = ['title']
    list_filter = ['order', 'create_time']
    list_editable = ['order']
    model_icon = 'fa fa-grav'


xadmin.site.register(HonorInfo, HonorInfoAdmin)
xadmin.site.register(AboutUs, AboutUsAdmin)