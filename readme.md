# django-drf的智能图像识别平台

目前只是demo,优化中

## 一.后端环境：

### 虚拟环境conda

conda create -n airec python=3.7
conda activate airec

pip install mod_wsgi  #因为使用apache部署，apache自动编译，或者安装编译好的包（需要apache），默认编译生成的路径c:\users\gly\appdata\local\pip\cache\wheels\2a\0d\51\d0c91a69c41e1c2ec5e8ac553173f78c2b6f3e2fb684330e9e

项目里有提供我的

参考我的博客http://www.berryha.com/blog/detail/33

### pip安装包

建议可以使用清华源-i https://pypi.tuna.tsinghua.edu.cn/simple some-package  

pip install django==3.2.14
pip install requests
pip install opencv-python
pip insatll numpy
pip install Pillow
pip install pymysql或者mysqlclient  #注意二选一,mysqlclient最好下载whl，有报错可能
pip install djangorestframework-jwt -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install drf-extensions
pip install django-redis

#待定阿里云支付
#pip install aliyun-python-sdk-core -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install djangorestframework -i https://pypi.tuna.tsinghua.edu.cn/simple  #drf
pip install django-cors-headers -i https://pypi.tuna.tsinghua.edu.cn/simple #跨域，需要配置

pip install django-filter  #过滤

pip install pytesseract tesseract #tesseract  #ocrdemo,需要tesseract ，效果差，建议使用百度ocrapi,后续换成自定义的部署的其他模型后可不装

#开发接口文档  drf-yasg或者coreapi，需要配置

pip install coreapi -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install drf-yasg -i https://pypi.tuna.tsinghua.edu.cn/simple



pip freeze > requirements.txt
pip install -r requirements.txt

## 二.mysql

登录数据库后执行

create database airec charset utf8;



## 三.前端，简单demo：

### 1.fronted文件夹下是html+static+js,给nginx

    <script src="static/js/jquery-3.6.0.min.js" type="text/javascript"></script>
### 2.templates文件夹是不分离的页面文件+static+js ,用于django自己render

    <script src="{% static 'js/jquery-3.6.0.min.js' %}" type="text/javascript"></script>

之所以这样是因为原来经过测试发现django无法相对路径导入static，导致django代码里写的render html报错
所以分开，两个文件夹下的静态文件路径配置不同

### 3.django/nginx两者都可使用

最后一点点调整了路径和settings配置，html写为类似
<!--    <script src="/static/js/jquery-3.6.0.min.js" type="text/javascript"></script>-->
开头多了个/,此时django/nginx两者都可使用
此处做个记录解决bug的过程,最后可以两个文件夹都添加到settings路径里

根据需要自行修改

建议使用nginx



## 四.git

#git init将该文件夹变成git可以管理的仓库
git init

#添加到暂存区
git add .

#提交到main分支
git commit -m 'firstcommit'  #-m后面的名字带空格可能会报错
#指定本地分支
git branch -M main

#github创建好远程仓库后
git remote add origin git@github.com:fireworkseasycold/airec.git
#推送到远程分支main
git push -u origin main  #成功后出现branch 'main' set up to track 'origin/main'.使用-u是为了在第一次推送时候将本地main分支和远程main分支联系起来，不会推送到远程新的main分支；之后可以只用git push origin main
另外
当git add 某个文件到缓存区，还没有git commit 但是你不想这个文件了
就可以使用git rm命令，两种选择：
git rm --cached “文件的位置或者路径” //会从git缓存中删除，但是不会物理的从硬盘删除；
git rm --f “文件的位置或者路径” //会从缓存中删除，还会直接从硬盘删除，连从垃圾箱找回的机会都不给你哦
git删除已经add的文件的两种方法：
用版本库内容清空暂存区，git reset HEAD （谨慎使用）
只把特定文件从暂存区删除，git rm --cached xxx
若删除已经添加缓存的某一个目录下所有文件的话需要添加一个参数 -r。
比如我要删除bin下面的已经加入缓存的所有文件，那我需要执行以下命令：
git rm -r --cached 废弃/

删除文件
（1）git rm test.txt
（2） git commit -m 'del_test.txt'
（3）git push origin main

使用.gitignore来排除不如要的，比如我新建个名为废弃的文件夹
git status命令是用来查看当前文件夹下的文件状态的
git log是用于查看文件上传日志的命令
git checkout
git checkout [需要下载的版本id]的作用是从本地仓库将之前上传的文件下载到工作区，一般配合git log使用，譬如我们将第一次上传的文件下载到工作区就需要使用git checkout 4e1eec290f384d2498de7c7e65ea3ba3469cf938命令，后头的一长串字符便是之前用git log命令查到的第一个版本的版本id，我们发现使用上述命令之后提示已回到了第一个版本，具体文件信息也已发生了更改，我在这里篇幅原因就不做演示了

## 五.说明

用户表{登录注册jwt注销,个人信息}

用户身份表 {图片，用户，关键点位置，人脸encoding}

图片库表

图像智能处理 {

​			ocr识别，

​			图片转pdf 
​            人脸处理 ：人脸识别

​			图片处理：动漫化 

​								待定二值化（黑白） 灰度化（灰色）
​            图片压缩  待定
​            }
图像处理任务管理  下载图片  进行的转化任务 上传 