#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views import generic

from blog.models import Category, Article, Tag

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
            article.content = markdown2.markdown(article.content, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，这里返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('name')
        # 调用 archive 方法，把获取的时间列表插入到 context 上下文中以便在模板中渲染
        kwargs['date_archive'] = Article.objects.archive()
        # tag_list 加入 context 里：
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)


class ArticleDetailView(generic.DetailView):
    # 指定视图获取哪个model
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"

    # 这里注意，pk_url_kwarg用于接收一个来自url中的主键，然后会根据这个主键进行查询
    pk_url_kwarg = 'article_id'

    # 指定以上几个属性，已经能够返回一个DetailView视图了，为了让文章以markdown形式展现，我们重写get_object()方法。
    # get_object() 返回该视图要显示的对象。
    # 如果有设置 queryset，该queryset 将用于对象的源；
    # 否则，将使用get_queryset(). get_object()从视图的所有参数中查找 pk_url_kwarg 参数；
    # 如果找到了这个参数，该方法使用这个参数的值执行一个基于主键的查询。
    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        obj.content = markdown2.markdown(obj.content, extras=['fenced-code-blocks'], )
        return obj


class CategoryView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        # 注意在url里我们捕获了分类的id作为关键字参数（cate_id）传递给了CategoryView，传递的参数在kwargs属性中获取。
        article_list = Article.objects.filter(category=self.kwargs['cate_id'], status='p')
        for article in article_list:
            article.content = markdown2.markdown(article.content, extras=['fenced-code-blocks'], )
        return article_list

    # 给视图增加额外的数据
    def get_context_data(self, **kwargs):
        # 增加一个category_list,用于在页面显示所有分类，按照名字排序
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(CategoryView, self).get_context_data(**kwargs)


class TagView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        """
        根据指定的标签获取该标签下的全部文章
        """
        article_list = Article.objects.filter(tags=self.kwargs['tag_id'], status='p')
        for article in article_list:
            article.content = markdown2.markdown(article.content, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(TagView, self).get_context_data(**kwargs)


class ArchiveView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        # 接收从url传递的year和month参数，转为int类型
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])
        # 按照year和month过滤文章
        article_list = Article.objects.filter(create_time__year=year, create_time__month=month)
        for article in article_list:
            article.content = markdown2.markdown(article.content, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(ArchiveView, self).get_context_data(**kwargs)
