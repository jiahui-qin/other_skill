from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Test(models.Model):
    '''
    这里建立一个test数据库，有三个字段：
    city char字段
    pepole integer字段
    author 作者，从contrib模块导入(测试此功能)
    '''
    city = models.CharField(max_length = 100)
    pepole = models.IntegerField()
    author = models.ForeignKey(User)

    '''
    创建数据库之后迁移数据库/创建数据库
    cmd下将当前文件置于manage.py下
    python manage.py makemigrations
    python manage.py migarte

    python manage.py sqlmigrate blog 0001 看当前操作执行的sql语句
    '''