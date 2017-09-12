#!/usr/bin/env python
# coding:utf-8
# @Time     : 17-9-11 下午11:11
# @Author   : w_di_sc
# @Site     : 
# @File     : urls.py
# @Software : PyCharm

from django.conf.urls import url

from . import views

app_name='blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),

]