#!/usr/bin/env python
# coding:utf-8
# @Time     : 17-9-13 下午10:42
# @Author   : w_di_sc
# @Site     : 
# @File     : blog_tags.py
# @Software : PyCharm
from ..models import  Post
from ..models import Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()