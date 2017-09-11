#!/usr/bin/env python
# coding:utf-8
# @Time     : 17-9-11 下午11:11
# @Author   : w_di_sc
# @Site     : 
# @File     : urls.py
# @Software : PyCharm

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]