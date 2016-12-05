#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICE = (
        ('d', 'Draft'),
        ('p', 'Published')
    )

    title = models.CharField('标题', max_length=70)
    content = models.TextField('正文')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICE)
    abstract = models.CharField('摘要', max_length=60, blank=True, null=True, help_text="可选，如若为空将摘选正文前60个字符")
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    category = models.ForeignKey(Category, verbose_name='分类', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']
