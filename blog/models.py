#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from collections import defaultdict


# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


class ArticleManage(models.Manager):
    """
    继承自默认的 Manager ，为其添加一个自定义的 archive 方法
    """

    def archive(self):
        # 获取到降序排列的精确到月份且已去重的文章发表时间列表
        # 并把列表转为一个字典，字典的键为年份，值为该年份下对应的月份列表
        date_list = Article.objects.datetimes('create_time', 'month', order='DESC')
        date_dict = defaultdict(list)
        for d in date_list:
            # 模板不支持defaultdict，因此我们把它转换成一个二级列表，由于字典转换后无序，因此重新降序排序
            date_dict[d.year].append(d.month)
        return sorted(date_dict.items(), reverse=True)


@python_2_unicode_compatible
class Article(models.Model):
    STATUS_CHOICE = (
        ('d', 'Draft'),
        ('p', 'Published')
    )

    # 仍然使用默认的 objects 作为 manager 的名字
    objects = ArticleManage()

    title = models.CharField('标题', max_length=70)
    content = models.TextField('正文')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICE)
    abstract = models.CharField('摘要', max_length=60, blank=True, null=True, help_text="可选，如若为空将摘选正文前60个字符")
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    """
    文章model中添加tag关系
    """
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


@python_2_unicode_compatible
class Tag(models.Model):
    """
    tag(标签)对应的数据库model
    """
    name = models.CharField('标签名', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name
