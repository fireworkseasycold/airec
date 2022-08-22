# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/8/15 6:22
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : savepic.py
# @Software: PyCharm
import base64
import datetime
import os

import cv2
import numpy as np
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_image(stream=None):
    """读取django的上传图片
    stream = request.FILES["image"]，例如xxx.css 类型<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
    返回 图像数据
    """
    data_temp = stream.read()
    image = np.asarray(bytearray(data_temp), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


def save2img(imgb64,pic_type='jpeg',path='cameraimg'):
    """
    将base64解码写入文件并使用当前时间保存,(建议放入异步任务)
    imgb64是字符串
    pic_type为保存的图片类型，默认jpeg
    """
    # import os
    #
    # print(os.getcwd()) # 打印出当前工作路径 ,用于No such file or directory
    save_result=False
    try:
        imagedata = base64.b64decode(imgb64)  # 解码为字节串
    except Exception as e:
        print(f'utils.imagetool.save2img函数解码失败，{e}')
        return save_result

    now = datetime.datetime.now()
    os.chdir(os.path.join(BASE_DIR,path)) #改变当前工作目录
    with open('img_{}.{}'.format(now.strftime("%Y%m%d%H%M%S"),pic_type), "wb") as f: #No such file or directory,os.getcwd()看工作路径
        f.write(imagedata)

    save_result=True
    # print('存储成功')
    return save_result

if __name__ == '__main__':
    print(os.path.abspath(__file__))  #查看当前文件的绝对路径，可以
    print(os.path.abspath('baiduapi.py'),Path(__file__))  #查看某个文件的绝对路径
    print(os.getcwd())
    # BASE_DIR = Path(__file__).resolve().parent.parent
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    s=os.path.join(BASE_DIR,'cameraimg')
    os.chdir(s)
    print(os.getcwd())


