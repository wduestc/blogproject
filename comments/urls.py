#!/usr/bin/env python
# coding:utf-8
# @Time     : 17-9-19 下午10:19
# @Author   : w_di_sc
# @Site     : 
# @File     : urls.py
# @Software : PyCharm
from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
]
