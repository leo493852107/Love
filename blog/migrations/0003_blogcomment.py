# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 05:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161206_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='\u8bc4\u8bba\u8005\u540d\u5b57')),
                ('user_email', models.EmailField(max_length=255, verbose_name='\u8bc4\u8bba\u8005\u90ae\u7bb1')),
                ('content', models.TextField(verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8bc4\u8bba\u53d1\u8868\u65f6\u95f4')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='\u8bc4\u8bba\u6240\u5c5e\u6587\u7ae0')),
            ],
        ),
    ]
