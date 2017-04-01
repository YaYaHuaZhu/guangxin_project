# -*- coding:utf-8 -*-
import xadmin
from xadmin import views

from models import IndexBanner, AboutBanner, InvestMentBanner, InvestProBanner
from models import NewsBanner, ContactBanner


class IndexBannerAdmin(object):
    list_display = ['name', 'background_video', 'banner_info', 'order', 'create_time']
    search_fields = ['name']
    list_filter = ['order', 'create_time']
    model_icon = 'fa fa-file-archive-o'


class AboutBannerAdmin(object):
    list_display = ['name', 'explain', 'order', 'create_time']
    search_fields = ['name']
    list_filter = ['order', 'create_time']
    model_icon = 'fa fa-file-archive-o'


class InvestMentBannerAdmin(object):
    list_display = ['name', 'explain', 'order', 'create_time']
    search_fields = ['name']
    list_filter = ['order', 'create_time']
    model_icon = 'fa fa-file-archive-o'


class InvestProBannerAdmin(object):
    list_display = ['name', 'explain', 'order', 'create_time']
    search_fields = ['name']
    list_filter = ['order', 'create_time']
    model_icon = 'fa fa-file-archive-o'


class NewsBannerAdmin(object):
    list_display = ['name', 'explain', 'order', 'create_time']
    search_fields = ['name']
    list_filter = ['order', 'create_time']
    model_icon = 'fa fa-file-archive-o'


class ContactBannerAdmin(object):
    list_display = ['name', 'explain', 'order', 'create_time']
    search_fields = ['name']
    list_filter = ['order', 'create_time']
    model_icon = 'fa fa-file-archive-o'


xadmin.site.register(IndexBanner, IndexBannerAdmin)
xadmin.site.register(AboutBanner, AboutBannerAdmin)
xadmin.site.register(InvestMentBanner, InvestMentBannerAdmin)
xadmin.site.register(InvestProBanner, InvestProBannerAdmin)
xadmin.site.register(NewsBanner, NewsBannerAdmin)
xadmin.site.register(ContactBanner, ContactBannerAdmin)
