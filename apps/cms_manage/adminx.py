# -*- coding:utf-8 -*-
import xadmin
from xadmin import views

from models import InvestMent, InvestProCategory, InvestPro, News, Contact


class GlobalSetting(object):
    site_title = "光信投资后台管理系统"
    site_footer = "Welkincity"
    menu_style = "accordion"


class InvestMentAdmin(object):
    list_display = ['name', 'description', 'create_time']
    search_fields = ['name']
    list_filter = ['create_time']
    model_icon = 'fa fa-tasks'


class InvestProCategoryAdmin(object):
    list_display = ['name', 'order', 'create_time']
    search_fields = ['name']
    list_filter = ['create_time']
    model_icon = 'fa fa-tasks'


class InvestProAdmin(object):
    list_display = ['title', 'category', 'create_time']
    search_fields = ['title']
    list_filter = ['category__name', 'create_time']
    model_icon = 'fa fa-tasks'


class NewsAdmin(object):
    list_display = ['title', 'create_time']
    search_fields = ['title']
    list_filter = ['create_time']
    model_icon = 'fa fa-tasks'


class ContactAdmin(object):
    list_display = ['name', 'address', 'order', 'create_time']
    search_fields = ['name']
    list_filter = ['order', 'create_time']
    model_icon = 'fa fa-tasks'

# xadmin.site.register(InvestMent, InvestMentAdmin)
xadmin.site.register(InvestProCategory, InvestProCategoryAdmin)
xadmin.site.register(InvestPro, InvestProAdmin)
xadmin.site.register(News, NewsAdmin)
xadmin.site.register(Contact, ContactAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)