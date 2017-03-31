from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponse
import json

from models import InvestMent, InvestProCategory, InvestPro, News
from banner_manage.models import IndexBanner, AboutBanner, InvestMentBanner
from banner_manage.models import InvestProBanner, NewsBanner, ContactBanner
# Create your views here.


class IndexView(View):
    def get(self, request):
        index_banner = IndexBanner.objects.all().order_by('-order')
        if index_banner:
            index_banner = index_banner[0]
        return render(request, "index.html", {
            "index_banner": index_banner
        })


class AboutView(View):
    def get(self, request):
        about_banner = AboutBanner.objects.all().order_by('-order')
        if about_banner:
            about_banner = about_banner[0]
        return render(request, "about.html", {
            "about_banner": about_banner
        })


class InvestMentView(View):
    def get(self, request):
        all_investment = InvestMent.objects.all()
        investment_banner = InvestMentBanner.objects.all().order_by('-order')
        if investment_banner:
            investment_banner = investment_banner[0]
        return render(request, "investment.html", {
            "investmenth": all_investment[:2],
            "investmentc": all_investment[2:],
            "investment_banner": investment_banner
        })


class InvestProjectView(View):
    def get(self, request):
        category = InvestProCategory.objects.all().order_by('-order')
        invest_pro = InvestPro.objects.all()
        type = request.GET.get('type', '')
        if type:
            invest_pro = invest_pro.filter(category=type)
        investpro_banner = InvestProBanner.objects.all().order_by('-order')
        if investpro_banner:
            investpro_banner = investpro_banner[0]
        return render(request, "investproject.html", {
            'category': category,
            'type': type,
            'invest_pro': invest_pro,
            'investpro_banner': investpro_banner
        })


class NewsView(View):
    def get(self, request):
        news = News.objects.all().order_by('-create_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(object_list=news, per_page=9, request=request)
        news = p.page(page)
        news_banner = NewsBanner.objects.all().order_by('-order')
        if news_banner:
            news_banner = news_banner[0]
        return render(request, "news.html", {
            'news': news,
            'news_banner': news_banner
        })


class NewsShowView(View):
    def get(self, request, news_id):
        news_show = News.objects.get(id=int(news_id))
        news_show = {
            "title": news_show.title,
            "content": news_show.content
        }
        return HttpResponse(json.dumps(news_show), content_type='application/json')


class ContactView(View):
    def get(self, request):
        contact_banner = ContactBanner.objects.all().order_by('-order')
        if contact_banner:
            contact_banner = contact_banner[0]
        return render(request, "contact.html", {
            'contact_banner': contact_banner
        })