# # !/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @Time : 2022/8/19 19:50
# # @Author : firworkseasycold
# # @Email : 1476094297@qq.com
# # @File : serializers.py
# # @Software: PyCharm
# from rest_framework import serializers
# from .models import ImageFileModel
#
# class ImageSerializer(serializers.ModelSerializer):
#     model=ImageFileModel
#     fields="__all__"
#     read_only_fields = ('image_name', 'image_path')
#
#     #重写
#
#     def validate(self, attrs):
#         getaction = self.context['view'].action
#         if getaction == 'create':
#             obj = ImageFileModel.objects.filter(file_name=attrs['image_file'].name)
#             if obj:
#                 raise serializers.ValidationError('存在相同文件名')
#             else:
#                 return attrs
#
#     def create(self, validated_data):
#         validated_data['image_name'] = validated_data['image_file'].name
#         return super().create(validated_data)