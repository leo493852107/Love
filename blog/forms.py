#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by Leo on 06/12/2016

from django import forms
from .models import Article, BlogComment


class BlogCommentForm(forms.ModelForm):
    """指定一些 Meta 选项以改变 form 被渲染后的样式"""

    class Meta:
        # form 关联的 Model
        model = BlogComment

        # fields 表示需要渲染的字段，这里需要渲染user_name、user_email、body
        # 这样渲染后表单会有三个文本输入框，分别是输入user_name、user_email、body的输入框
        fields = ['user_name', 'user_email', 'content']

        # 为各个需要渲染的字段指定渲染成什么html组件，主要是为了添加css样式。
        # 例如 user_name 渲染后的html组件如下：
        # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入昵称',
                'aria-describedby': 'sizing-addon1',
            }),
            'user_email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入邮箱',
                'aria-describedby': 'sizing-addon1',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': '我来点评两句~'
            }),
        }
