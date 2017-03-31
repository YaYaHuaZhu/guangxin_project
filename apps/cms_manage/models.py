# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField


# InvestMent Model
class InvestMent(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"姓名")
    name_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"姓名（英文）")
    photo = models.ImageField(upload_to="investment/%Y/%m/%d", verbose_name=u"个人照片（375*375）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（越大优先级越高）")
    description = models.TextField(verbose_name=u"个人描述")
    description_en = models.TextField(blank=True, null=True, verbose_name=u"个人描述（英文）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"投资团队"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class InvestProCategory(models.Model):
    name = models.CharField(max_length=40, verbose_name=u"类别名称")
    name_en = models.CharField(max_length=40, blank=True, null=True, verbose_name=u"类别名称（英文）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（越大优先级越高）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"投资项目类别"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class InvestPro(models.Model):
    category = models.ForeignKey(InvestProCategory, verbose_name=u"投资项目类型")
    title = models.CharField(max_length=50, verbose_name=u"投资项目名称")
    title_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"投资项目名称（英文）")
    photo = models.ImageField(upload_to="investpro/%Y/%m/%d", verbose_name=u"项目图片（450*450）")
    http_url = models.URLField(blank=True, null=True, verbose_name=u"项目网址")
    description = models.TextField(verbose_name=u"项目描述")
    description_en = models.TextField(blank=True, null=True, verbose_name=u"项目描述（英文）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（越大优先级越高）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"投资项目"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    title_en = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"标题（英文）")
    photo = models.ImageField(upload_to="news/%Y/%m/%d", verbose_name=u"新闻封面（450*300）")
    content = RichTextUploadingField(verbose_name=u"内容")
    content_en = RichTextUploadingField(blank=True, null=True, verbose_name=u"内容（英文）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"新闻报道"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"名称（标识）")
    address = models.CharField(max_length=100, verbose_name=u"地址")
    address_en = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"地址（英文）")
    phone = models.CharField(max_length=100, verbose_name=u"电话")
    fax = models.CharField(max_length=100, verbose_name=u"传真")
    business_email = models.EmailField(verbose_name=u"商业联系邮箱")
    hr_email = models.EmailField(verbose_name=u"人事招聘邮箱")
    order = models.IntegerField(default=0, verbose_name=u"顺序（只会显示顺序值最高的一组信息）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"联系我们"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
