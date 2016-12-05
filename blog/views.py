#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views import generic

from blog.models import Category, Article

import markdown2


# Create your views here.
class IndexView(generic.ListView):
    """
    首页视图,继承自ListVIew，用于展示从数据库中获取的文章列表
    """

    # template_name属性用于指定使用哪个模板进行渲染
    template_name = "blog/index.html"

    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = "article_list"

    def get_queryset(self):
        """
        过滤数据，获取所有已发布文章，并且将内容转成markdown形式
        """
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            # 将markdown标记的文本转为html文本
            article.content = markdown2.markdown(article.content, )
        return article_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，这里返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
