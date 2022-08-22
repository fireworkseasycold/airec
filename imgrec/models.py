from django.db import models
# Create your models here.



user_sex=(
        ('P','公开'),
        ('H','隐藏'),
    )

class ImageFileModel(models.Model):
    user = models.ForeignKey('user.AUser', on_delete=models.CASCADE, verbose_name='图库用户', help_text='图库用户')
    image_file = models.ImageField(verbose_name='图片', upload_to='image/%Y%m%d',blank=True,default='imgagepath',help_text='图片路径')
    create_dt = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    modify_dt = models.DateTimeField(auto_now=True, verbose_name='修改时间', help_text='修改时间')
    status=models.CharField(max_length=1,choices=user_sex,default='P',verbose_name='是否可见',help_text='是否可见')

    class Meta:
        db_table='imagefile'
        verbose_name =verbose_name_plural = '图像库'


    def __str__(self):
        return self.image_file.name

    @property
    def image_file_url(self):  # 这一段很关键要加上
        if self.image_file and hasattr(self.image_file, 'url'):
            return self.image_file.url
