from rest_framework import serializers
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from .models import ImageFileModel
from .serializers import ImageSerializer
# Create your views here.

class FileViewSet(ModelViewSet):
    parser_classes = (MultiPartParser,)#為swagger能夠測試出是上傳文件
    queryset = ImageFileModel.objects.all()
    serializer_class = ImageSerializer




