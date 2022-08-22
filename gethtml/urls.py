# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/8/3 19:19
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : urls.py
# @Software: PyCharm
from django.urls import path

from . import views

urlpatterns=[
    path("getcameraform", views.getcameraform),
    path("getcamerajson",views.getcamerajson),
    path("getcameraformdrf",views.getcameraformdrf),
    path("getcamerajsondrf",views.getcamerajsondrf),
    path("ocrdemo",views.ocrdemo),
]