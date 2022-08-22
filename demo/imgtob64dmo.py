# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/8/22 8:32
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : imgtob64dmo.py
# @Software: PyCharm
import base64
import cv2

testimg="testimg/who.jpg"
#通过opencv转base64
img_im= cv2.imread(testimg)
aa=base64.b64encode(cv2.imencode('.jpg',img_im)[1]).decode()
# print(aa)
print(f"aa={len(aa)}")


#通过bytes再转base64
bb=base64.b64encode(open(testimg, 'rb').read())
# print(bb)
print(f"bb={len(bb)}")

# aa=307432
# bb=160496