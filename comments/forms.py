#!/usr/bin/env python
# coding:utf-8
# @Time     : 17-9-13 下午11:24
# @Author   : w_di_sc
# @Site     : 
# @File     : forms.py
# @Software : PyCharm
from django import forms
from .models import Comment

#Django的表单类必须继承自forms.Form类或者forms.ModelForm类
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']