from django.shortcuts import render

# Create your views here.

# face
def getcameraform(request):
    """获取表单提交的数据页面
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8"""
    return render(request,'getcameraform.html')


def getcamerajson(request):
    """获取json提交数据页面
    """
    return render(request,'getcamerajson.html')


def getcameraformdrf(request):
    """获取表单提交的数据页面
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8"""
    return render(request,'getcameraformdrf.html')

def getcamerajsondrf(request):
    """获取json提交数据页面
    """
    return render(request,'getcamerajsondrf.html')

#ocr
def ocrdemo(request):
    """获取json提交数据页面
    """
    return render(request,'ocrdemo.html')
