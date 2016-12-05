#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by Leo on 05/12/2016

from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]

