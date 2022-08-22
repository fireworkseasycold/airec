# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/8/22 8:24
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : sendbase64.py
# @Software: PyCharm




"""模拟前后端发送base64"""
# 1.第一种 ‘form/data’：
# 客户端：
import base64
import json

import cv2
import numpy as np
import requests


# url='http://127.0.0.1:8000/face/receivecamera'
# image1 = cv2.imread("testimg/who.jpg")
# aa = base64.b64encode(cv2.imencode('.jpg', image1)[1]).decode()
# # print(aa)
# #我这里接口实际上接收的约定数据是{picture:"data:image/jpeg;base64,xxx"}
# print('开始模拟post')
# response = requests.post(url, data={"picture":'data:image/jpeg;base64,'+aa})
# print(response.content.decode("utf-8"))  #因为我后端有get方法渲染页面，这里也会带上页面
# print(response.text)
# print(response.content)
# print(response)
# print("请求头:%s" %r.request.headers)
# print("响应头:%s" %r.headers)

#
#
# # 服务端：
# def image_base64(request):
#     result = request.POST.get("picture")
#     img_byte = base64.b64decode(result)
#     img_np_arr = np.fromstring(img_byte, np.uint8)
#     image = cv2.imdecode(img_np_arr, cv2.IMREAD_COLOR)



# image 已经转为矩阵了
# 2.第二种‘application/json’:
# 客户端：
url2='http://127.0.0.1:8000/face/receivecamerajson'
image1 = cv2.imread("testimg/who.jpg")
bb= base64.b64encode(cv2.imencode('.jpg', image1)[1]).decode()
r = requests.post(url2, json={"picture": 'data:image/jpeg;base64,'+bb})

print(r.content.decode("utf-8"))
print("请求头:%s" %r.request.headers)
print("响应头:%s" %r.headers)


# 服务端：
def local_ocr_base64(request):
    # result = request.POST.get("image")
    data = request.body
    data_json = json.loads(data)  # data是str格式的，需要转为json
    result = data_json["picture"]
    img_byte = base64.b64decode(result)
    img_np_arr = np.fromstring(img_byte, np.uint8)
    image = cv2.imdecode(img_np_arr, cv2.IMREAD_COLOR)
#
# 分开为两个文件，一个客户端一个服务端口
# 不如postman或者html的访问方便