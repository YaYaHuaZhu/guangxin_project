# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-01 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(default='', upload_to='about_us/%Y/%m', verbose_name='\u80cc\u666f\u56fe\u7247\uff08700*510\uff09'),
        ),
        migrations.AddField(
            model_name='honorinfo',
            name='image',
            field=models.ImageField(default='', upload_to='honor/%Y/%m', verbose_name='\u80cc\u666f\u56fe\u7247\uff08960*540\uff09'),
        ),
    ]