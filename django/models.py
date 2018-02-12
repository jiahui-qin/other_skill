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

    def __str__(self):
        return self.city

    '''
    创建数据库之后迁移数据库/创建数据库
    cmd下将当前文件置于manage.py下
    python manage.py makemigrations
    python manage.py migarte

    python manage.py sqlmigrate blog 0001 看当前操作执行的sql语句
    '''

    '''
    往数据库中写入数据：
    python manage.py shell #打开交互式的命令行界面
    from blog.models import Test
    c = Test(city = 'Xiamen', pepole = 34000) 
    c.save()#会报错，因为没有指定user(author)

    ## 创建一个User
    python manage.py createsuperuser # 按照步骤创建用户
    from blog.models import Test
    from django.utils import timezone # 时间
    from django.contrib.auth.models import User # 导入用户系统
    c = Category.objects.get(name='category test') #如果要导入其他相关表需要先import

    '''