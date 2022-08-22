from django.db import models
# from imgrec.models import ImageFileModel
from django.contrib.auth.models import AbstractUser
# # Create your models here.
#
# # User                    1   1
# # Faceidcard              1       1
# # ImageFileModel              n   1
#
class AUser(AbstractUser):
    """用户表单"""
    id=models.IntegerField(verbose_name='用户id',help_text='用户id',primary_key=True)
    username=models.CharField(max_length=128,verbose_name='用户名',help_text='用户名',unique=True)
    password=models.CharField(max_length=128,verbose_name='密码',help_text='用户密码')
    email=models.EmailField(verbose_name='邮箱',help_text='用户邮箱',unique=True)
    # mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号',help_text='用户手机号')

    class Meta:
        db_table='auser'
        verbose_name = verbose_name_plural = '用户'
    # 在 str 魔法方法中, 返回用户名称
    def __str__(self):
        return self.username






class Faceidcard(models.Model):
    """用户人脸识别数据表"""
    faceimg=models.ImageField(verbose_name='刷脸图片',upload_to='faceidcard/%Y%m%d',default='',blank=True,help_text='刷脸图片')
    user=models.OneToOneField('user.AUser',related_name='faceidcard_user',verbose_name='刷脸用户',on_delete=models.CASCADE)
    chin=models.CharField(max_length=128,verbose_name='下巴',default=[],help_text='下巴')
    left_eyebrow=models.CharField(max_length=128,verbose_name='左眉',default=[],help_text='左眉')
    right_eyebrow=models.CharField(max_length=128,verbose_name='右眉',default=[],help_text='右眉')
    nose_bridge=models.CharField(max_length=128,verbose_name='鼻桥',default=[],help_text='鼻桥')
    nose_tip=models.CharField(max_length=128,verbose_name='鼻尖',default=[],help_text='鼻尖')
    left_eye=models.CharField(max_length=128,verbose_name='左眼',default=[],help_text='左眼')
    right_eye=models.CharField(max_length=128,verbose_name='右眼',default=[],help_text='右眼')
    top_lip=models.CharField(max_length=128,verbose_name='上唇',default=[],help_text='上唇')
    bottom_lip=models.CharField(max_length=128,verbose_name='下唇',default=[],help_text='下唇')
    face_encoding=models.CharField(max_length=128,verbose_name='刷脸编码',default=[],help_text='128位人脸编码')

    class Meta:
        db_table='faceidcard'
        verbose_name = verbose_name_plural = '用户人脸数据'

    # 在 str 魔法方法中, 返回用户名称
    def __str__(self):
        return self.user
#
# # chin [(65, 105), (65, 116), (66, 127), (67, 139), (70, 150), (76, 161), (84, 169), (93, 177), (105, 180), (118, 179), (131, 173), (143, 166), (153, 157), (158, 145), (160, 132), (161, 119), (162, 106)]
# # left_eyebrow [(69, 93), (74, 88), (81, 87), (89, 88), (96, 91)]
# # right_eyebrow [(112, 92), (121, 89), (130, 87), (139, 88), (147, 93)]
# # nose_bridge [(103, 102), (102, 110), (101, 118), (100, 126)]
# # nose_tip [(93, 133), (97, 134), (101, 135), (107, 134), (113, 133)]
# # left_eye [(76, 103), (81, 99), (87, 100), (92, 104), (86, 105), (80, 105)]
# # right_eye [(120, 104), (125, 100), (132, 100), (137, 103), (132, 105), (125, 105)]
# # top_lip [(87, 148), (92, 146), (98, 144), (102, 146), (107, 144), (115, 146), (124, 148), (121, 148), (107, 148), (102, 149), (98, 149), (89, 149)]
# # bottom_lip [(124, 148), (115, 153), (108, 156), (102, 156), (97, 156), (92, 154), (87, 148), (89, 149), (98, 149), (102, 149), (107, 149), (121, 148)]


# class ImageTask(models.Model):
# """图片操作任务"""
# status={
#     '0':'未开始',
#     '1':'已完成',
#     '2':'进行中',
# }
