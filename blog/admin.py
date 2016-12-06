#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import Category, ArticleManage, Article, Tag


class CategoryInline(admin.StackedInline):
    model = Category


class TagInline(admin.StackedInline):
    model = Tag
    extra = 3


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('title', {'fields': ['title']}),
        ('content', {'fields': ['content']}),
        ('status', {'fields': ['status']}),
        ('abstract', {'fields': ['abstract']}),
        ('views', {'fields': ['views']}),
        ('likes', {'fields': ['likes']}),
        ('topped', {'fields': ['topped']}),
        ('category', {'fields': ['category']}),
        ('tags', {'fields': ['tags']}),
    ]



admin.site.register(Article, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
