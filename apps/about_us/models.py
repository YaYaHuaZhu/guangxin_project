# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.


class AboutUs(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"展示标题")
    title_en = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"展示标题（英文）")
    explain = models.TextField(u"描述文字")
    explain_en = models.TextField(null=True, blank=True, verbose_name=u"描述文字（英文）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（只显示顺序值最大的内容）")
    image = models.ImageField(upload_to="about_us/%Y/%m", default="", verbose_name=u"背景图片（700*510）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"关于我们内容"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class HonorInfo(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"展示标题")
    title_en = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"展示标题（英文）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（只显示顺序值最大的内容）")
    image = models.ImageField(upload_to="honor/%Y/%m", default="", verbose_name=u"背景图片（960*540）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"荣誉展示视图"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Honors(models.Model):
    own = models.ForeignKey(HonorInfo, verbose_name=u"所属")
    name = models.CharField(max_length=200, verbose_name=u"荣誉名称")
    name_en = models.CharField(max_length=200, null=True, blank=True, verbose_name=u"荣誉名称（英文）")
    order = models.IntegerField(default=0, verbose_name=u"顺序（只显示顺序值最大的8条内容）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"荣誉"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name