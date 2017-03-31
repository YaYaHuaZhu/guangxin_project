# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.


class IndexBanner(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"名称（识别作用）")
    background_video = models.FileField(upload_to="index_banner/%Y/%m", verbose_name=u"背景视频（MP4格式）")
    banner_info = models.ImageField(upload_to="index_banner/%Y/%m", verbose_name=u"浮出图片（建议1300*350左右）")
    banner_info_en = models.ImageField(null=True, blank=True, upload_to="index_banner/%Y/%m", verbose_name=u"浮出图片（英文页面1300*350左右）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（只会显示顺序值最高的一套Banner）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"首页Banner管理"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class AboutBanner(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"标题")
    name_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"标题（英文）")
    explain = models.TextField(verbose_name=u"描述")
    explain_en = models.TextField(blank=True, null=True, verbose_name=u"描述（英文）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（只会显示顺序值最高的一套Banner）")
    banner_bg = models.ImageField(upload_to="about_banner/%Y/%m", verbose_name=u"背景图片（1920*875）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"关于我们Banner管理"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class InvestMentBanner(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"标题")
    name_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"标题（英文）")
    explain = models.TextField(verbose_name=u"描述")
    explain_en = models.TextField(blank=True, null=True, verbose_name=u"描述（英文）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（只会显示顺序值最高的一套Banner）")
    banner_bg = models.ImageField(upload_to="about_banner/%Y/%m", verbose_name=u"背景图片（1920*875）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"投资团队Banner管理"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class InvestProBanner(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"标题")
    name_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"标题（英文）")
    explain = models.TextField(verbose_name=u"描述")
    explain_en = models.TextField(blank=True, null=True, verbose_name=u"描述（英文）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（只会显示顺序值最高的一套Banner）")
    banner_bg = models.ImageField(upload_to="about_banner/%Y/%m", verbose_name=u"背景图片（1920*875）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"投资项目Banner管理"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class NewsBanner(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"标题")
    name_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"标题（英文）")
    explain = models.TextField(verbose_name=u"描述")
    explain_en = models.TextField(blank=True, null=True, verbose_name=u"描述（英文）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（只会显示顺序值最高的一套Banner）")
    banner_bg = models.ImageField(upload_to="about_banner/%Y/%m", verbose_name=u"背景图片（1920*875）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"新闻报道Banner管理"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class ContactBanner(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"标题")
    name_en = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"标题（英文）")
    explain = models.TextField(verbose_name=u"描述")
    explain_en = models.TextField(blank=True, null=True, verbose_name=u"描述（英文）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（只会显示顺序值最高的一套Banner）")
    banner_bg = models.ImageField(upload_to="about_banner/%Y/%m", verbose_name=u"背景图片（1920*875）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"联系我们Banner管理"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
