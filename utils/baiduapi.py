# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/8/15 4:35
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : baiduapi.py
# @Software: PyCharm
import base64

import requests

from utils.imagetool import save2img


def get_accesstoken():
    """
    获取百度api的access_token
    :return:
    """
    # 请求URL
    AK='prvGrOXLTGhhTzn9Zu0wG9lK'
    SK='tzG5jGsmtuRfVibomdYrGGsZ3zRRurlo'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(AK,SK)
    response = requests.get(host)
    if response:
        response_dict=response.json()
        # print(response_dict)
        return response_dict['access_token']
    else:
        return {'error':'no token'}



def get_cartoon_img(img):
    """
    获取百度图像二维化处理的图像信息
    :param img:图片路径
    :return:
    """
    # 请求URL
    url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime'
    # 获取图像信息
    origin_img = open(file=img, mode='rb')
    # 将图片进行base64编码
    img = base64.b64encode(origin_img.read())
    # 关闭图像
    origin_img.close()
    # 请求header信息
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    # 请求Params
    params = {
        'access_token': get_accesstoken(),
        'image': img
    }
    # 获取请求结果
    res = requests.post(url=url, data=params, headers=headers)
    # 处理响应结果
    # print(res)
    # print(res.json())
    # print(res.json().keys())
    try:
        imgb64=res.json()['image']  #"base64的字符串，已经去掉了base64的头"
        # print(imgb64)
        return imgb64
    except Exception as e:
        return e


if __name__ == '__main__':
    print('开始百度ocrapi')
    imgbase64=get_cartoon_img(img='testimg/who.jpg')
    # print(imgbase64)
    save2img(imgbase64)