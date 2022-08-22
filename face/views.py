import base64
import datetime
import json
import re
import time
from io import BytesIO
# 导入所需要的库
import requests
import base64

import cv2
import numpy
from django.http import JsonResponse, request, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.imagetool import save2img

# Create your views here.

#客户端postman or html or sendbase64demo



# django原生写法
# def receivecameraform(request):
#     """
#     表单提交数据
#     :param request:
#     :return:
#     """
#     if request.method == "POST":
#         # request.POST(只能获取表单数据)
#         # 请求标头application/x-www-form-urlencoded; charset=UTF-8
#         camera_data=request.POST.get("picture") #是个str数据为'data:image/jpeg;base64,xxxstrxxxxxxxxx'
#         print(camera_data)
#         #写法1：# imgb64=camera_data[23:]  #如果格式不变则可将此直接数据切片23为jpeg索引,png为22
#         #写法2 更通用
#         # camera_datalist=camera_data.split(';base64,')  #切片
#         # # print(camera_datalist)
#         # pic_type=camera_datalist[0].replace('data:image/','')
#         # imgb64=camera_datalist[1]
#         #写法3
#         camera_datalist=re.split('data:image/|;base64,',camera_data)
#         # print(camera_datalist) #三个字符串组成的列表
#         pic_type=camera_datalist[1]
#         imgb64=camera_datalist[2]
#         save2img(imgb64,pic_type)
#
#
#         return JsonResponse({'code': 200,'data': 'ajax-post传参图片数据是：{0}'.format(imgb64)})
#
# def receivecamerajson(request):
#     """
#     json提交数据
#     :param request:
#     :return:
#     """
#     if request.method == "POST":
#         param_b = request.body  # django原生的属性request.body(获取非表单数据)
#         # param_b=b'{"picture":"data:image/jpeg;base64,xxxxxxxx"}
#         # print(param_b) #type=<class 'bytes'>
#
#         param_dict = json.loads(param_b)  # 将json格式数据转换为python字典类型,即对对象进行json decode解码也叫反序列化
#         # print(param_dict) #type=dict
#         return JsonResponse({'code': 200,'data': 'ajax-post传参返回的json图片数据是：{0}'.format(param_dict)},json_dumps_params={'ensure_ascii': False})

#drf写法
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer, BrowsableAPIRenderer




# drf写法
@api_view(['post','get'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))  #如果不使用这里的render和template_name,可以两者都去掉，同时注释get；这里等同于get_htmlapp里的，都有则使用第一个
def receivecameraform(request):
    """
    form提交数据
    """
    camera_data = request.data
    # print(camera_data)
    return Response({'msg':'200'}, template_name='getcameraform.html')

@api_view(['post','get'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer,BrowsableAPIRenderer])  #如果不使用这里的render和template_name,可以两者都去掉，同时注释get；这里等同于get_htmlapp里的
def receivecamerajson(request):
    """
    json提交数据
    """
    camera_data = request.data
    # print(camera_data)
    return Response({'msg':'200'}, template_name='getcamerajson.html')


# cbv -APIView
class FacecameraFormAPIView(APIView):
    renderer_classes=[TemplateHTMLRenderer, JSONRenderer] #template_name，不带这句和下方的template_name就是默认的restframework的api.html页,即BrowsableAPIRenderer
    def post(self,request):
        """
        #request.data    QueryDict:{'picture':['data:image/jpeg;base64,xxxstrxxxxxxxxx']}
        """

        camera_data = request.data.get("picture")  # camera_data是个str数据为'data:image/jpeg;base64,xxxstrxxxxxxxxx'
        # print(camera_data)
        #写法1：# imgb64=camera_data[23:]  #如果格式不变则可将此直接数据切片23为jpeg索引,png为22
        #写法2 更通用
        # camera_datalist=camera_data.split(';base64,')  #切片
        # # print(camera_datalist)
        # pic_type=camera_datalist[0].replace('data:image/','')
        # imgb64=camera_datalist[1]
        #写法3 最通用
        camera_datalist=re.split('data:image/|;base64,',camera_data)
        # print(camera_datalist) #三个字符串组成的列表,第一个为空
        pic_type,imgb64=camera_datalist[1],camera_datalist[2]
        save2img(imgb64,pic_type)
        return Response({'msg':'200'},template_name='getcameraformdrf.html') #如上面使用了render_classes,没有template_name会报错

    def get(self,request):
        return Response({'msg': 'ok'},template_name='getcameraformdrf.html')


class FacecameraJsonAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer,JSONRenderer]

    def post(self, request):
        camera_data = request.data
        print(camera_data)
        return Response({'msg': '200'},template_name='getcameraformdrf.html')  # 如上面使用了render_classes,没有template_name会报错

    def get(self, request):
        return Response({'msg': 'ok'}, template_name='getcameraformdrf.html')




