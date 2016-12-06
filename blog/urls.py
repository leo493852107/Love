#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by Leo on 05/12/2016

from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<article_id>\d+)$', views.CategoryView.as_view(), name='category'),
]
