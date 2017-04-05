"""guangxin_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from guangxin_project.settings import MEDIA_ROOT, STATIC_ROOT
import xadmin

from cms_manage.views import IndexView, AboutView, InvestMentView, InvestProjectView, NewsView
from cms_manage.views import ContactView, NewsShowView, page_not_found, page_error
from cms_manage.views import EnIndexView, EnAboutView, EnInvestMentView, EnInvestProjectView, EnNewsView
from cms_manage.views import EnContactView, EnNewsShowView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^manage/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^en/$', EnIndexView.as_view(), name="en_index"),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^en/about/$', EnAboutView.as_view(), name="en_about"),
    url(r'^investment/$', InvestMentView.as_view(), name="investment"),
    url(r'^en/investment/$', EnInvestMentView.as_view(), name="en_investment"),
    url(r'^investproject/$', InvestProjectView.as_view(), name="investproject"),
    url(r'^en/investproject/$', EnInvestProjectView.as_view(), name="en_investproject"),
    url(r'^news/$', NewsView.as_view(), name="news"),
    url(r'^en/news/$', EnNewsView.as_view(), name="en_news"),
    url(r'^news/(?P<news_id>\d+)$', NewsShowView.as_view(), name="news_show"),
    url(r'^en/news/(?P<news_id>\d+)$', EnNewsShowView.as_view(), name="en_news_show"),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^en/contact/$', EnContactView.as_view(), name="en_contact"),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls'))
]

handler404 = page_not_found
handler500 = page_error