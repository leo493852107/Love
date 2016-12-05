#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone


# Create your models here.




@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# class Blog(models.Model):
#     name = models.CharField(max_length=50)
#     summary = models.CharField(max_length=200)
#     content = models.TextField()
#     create_at = models.DateField('date published')
#
#
# class Comment(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     content = models.TextField()
#     create_at = models.DateField('date published')


# class Blog(models.Model):
#     user_id = models.CharField(max_length=50)
#     user_name = models.CharField(max_length=50)
#     user_image = models.CharField(max_length=500)
#     name = models.CharField(max_length=50)
#     summary = models.CharField(max_length=200)
#     content = models.TextField()
#     create_at = models.DateField('date published')
#
#
# class Comment(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     user_id = models.CharField(max_length=50)
#     user_name = models.CharField(max_length=50)
#     user_image = models.CharField(max_length=500)
#     content = models.TextField()
#     create_at = models.DateField('date published')
