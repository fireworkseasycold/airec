# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/8/2 18:50
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : urls.py
# @Software: PyCharm
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns=[
    path('receivecamera',views.receivecameraform),  #未指定则为默认form
    path('receivecamerajson',views.receivecamerajson), #指定为json
    #APIView
    path('receivecameradrf',views.FacecameraFormAPIView.as_view()),
    path('receivecamerajsondrf',views.FacecameraJsonAPIView.as_view()), #获取camera
#     path('detect',views.face_detect), #人脸检测+定位
#     path('compare',views.face_compare),#人脸比对
#     path('similar',views.face_simliar),#查找相似人脸
]





