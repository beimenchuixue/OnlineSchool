from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户信息表，并扩展了django默认user表，
    还需要再setting中配置 AUTH_USER_MODEL = 'users.UserProfile'
    用这张扩展的表替换django默认的用户表，需要注意点不能在工程开始就初始化表工作，
    这会和这张表冲突并发送不可描叙的错误，这酸爽，你懂得
    """
    sex = (
        ('male', '男'),
        ('female', '女')
    )
    nick_name = models.CharField(max_length=50, verbose_name='昵称')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    gender = models.CharField(max_length=6, choices=sex, default='male', verbose_name='性别')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')
    head_image = models.ImageField(upload_to='image/%Y/%m', default='default.png', max_length=100, verbose_name='头像')

    add_time = models.DateTimeField(auto_now_add=True, editable=False, blank=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def unread_num(self):
        """
        获取全局的一个消息数通知
        如果其他想要加入request全局的参数，都需要在此写上对应的方法
        """
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()


class Banner(models.Model):
    """
    网页首页轮播图，包含标题、图片、对应url地址、优先级信息
    """
    title = models.CharField(max_length=20, verbose_name='标题')
    banner_image = models.ImageField(max_length=50, upload_to='banner/%Y/%m', verbose_name='轮播图')
    index = models.IntegerField(default=100, verbose_name='顺序')
    url = models.URLField(max_length=200, verbose_name='网页地址')
    is_up = models.BooleanField(default=False, verbose_name='是否轮播')

    add_time = models.DateTimeField(auto_now_add=True, editable=True, blank=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class UPBanner(Banner):
    """上架轮播图"""
    class Meta:
        verbose_name = '上架轮播图'
        verbose_name_plural = verbose_name
        proxy = True


class DownBanner(Banner):
    """下架轮播图"""
    class Meta:
        verbose_name = '上架轮播图'
        verbose_name_plural = verbose_name
        proxy = True


class EmailVerifyRecord(models.Model):
    """
    邮箱验证码，包含信息有验证码、邮箱地址、发送类型（注册或忘记密码）、发送时间
    """
    email_type = (
        ('register', '注册'),
        ('forget', '忘记密码'),
        ('update', '修改邮箱')
    )
    code = models.CharField(max_length=36, verbose_name='验证码')
    email = models.EmailField(max_length=100, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=email_type, verbose_name='验证类型')
    send_time = models.DateTimeField(auto_now_add=True, editable=False, blank=True, verbose_name='发送时间')
    has_used = models.BooleanField(default=False, verbose_name='是否已经使用')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email
