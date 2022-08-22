import cv2
import numpy as np
import pytesseract
from PIL import Image
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer

from rest_framework.response import Response




# @csrf_exempt  # 用于规避跨站点请求攻击
from utils.imagetool import read_image

#django原生
# def ocrapi(request):
#     """
#
#     post:multipart/form-data; boundary=----WebKitFormBoundaryOTfqBbkJkptSFlUH
#
#     """
#     result = {"code": None}
#     if request.method == "POST":
#         # print('开始判断是否有图')
#         if request.FILES.get("image", None) is not None:
#             # print(request.FILES["image"]) #xxx,jpg
#             img = read_image(stream=request.FILES["image"])
#             # print('选择图片上传成功')
#             # print(img)
#             # OpenCV转PIL
#             img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#             # print('转pil')
#             # print(img)
#             # 执行tesseract-ocr识别
#             rec_result = pytesseract.image_to_string(img, lang='chi_sim')
#             # print(rec_result)
#             # print(rec_result)
#             result.update({"code": 200,"output": rec_result})
#         else:
#             result.update({"code": 10011,"msg":"未上传图片","output": '请上传图片'})
#     return JsonResponse(result)

# drf
@api_view(['post','get'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer,BrowsableAPIRenderer])  #都有则为第一个,
def ocrapi(request):
    result = {"code": None}
    if request.FILES.get("image", None) is not None:
        # print(request.FILES["image"]) #xxx.jpg
        # print(type(request.FILES["image"])) #<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
        img = read_image(stream=request.FILES["image"])
        # print('选择图片上传成功')
        # print(img)
        # OpenCV转PIL
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # print('转pil')
        # print(img)
        # 执行tesseract-ocr识别
        rec_result = pytesseract.image_to_string(img, lang='chi_sim')
        # print(rec_result)
        # print(rec_result)
        result.update({"code": 200,"msg":"识别成功","output": rec_result})
    else:
        result.update({"code": 10011,"msg":"未上传图片","output": '请上传图片'})
    return Response(result)