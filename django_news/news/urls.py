# -*- coding: UTF-8 -*-
"""
接着，要让路由系统能够访问到刚才写好的视图函数。因此先实现子应用 news 的路由表，创建 news/urls.py 文件如下：
"""
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login),
    path('user/list/', views.user_list, name='user_list'),
    path('user/add/', views.user_add, name='user_add'),
    path('something/', views.something, name='something')
]