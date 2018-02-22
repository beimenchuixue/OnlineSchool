"""
Django settings for OnlineSchool project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h@(=9&d-&!1$#45_w7t9oa9%%3_w8okxzy@cs8^ff-ivblw9ra'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# 把apps目录添加到环境搜索路径，这个apps用于归类django本身的app
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# 把 extra_apps添加到到环境搜索路径，extra_apps用于存放第三方app
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # django对request请求进行拦截找sessionid
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 用户app
    'users.apps.UsersConfig',
    # 课程app
    'course.apps.CourseConfig',
    # 课程机构app
    'organization.apps.OrganizationConfig',
    # 用户操作app
    'operation.apps.OperationConfig',
    # 对于以上注册app，也可以直接使用app的名字也行

    # 第三方xadmin注册
    'xadmin',
    # githup下载地址： https://github.com/sshwsfc/xadmin/tree/django2
    # 找到分支，下载django2对应分支的项目，并把xadmin拷贝到extra_apps中
    'crispy_forms',
    # 简单验证码app，需要数据库存放图片路径的表，需要初始化表操作
    'captcha',
    # 分页功能app
    'pure_pagination',
]

# 添加这个设置，用users中的UserProfile替换django默认的用户表
AUTH_USER_MODEL = 'users.UserProfile'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OnlineSchool.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # django中设置图片的上下文地址
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'OnlineSchool.wsgi.application'

# 自定义 authenticate验证
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onlineschool',
        'USER': 'onlineschool',
        'PASSWORD': '123456',
        'HOST': '10.0.0.220'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# 语言设置为中文
LANGUAGE_CODE = 'zh-hans'

# 时区设置为东八区，上海和北京在同一个时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 禁止使用UTC时间，如何不为false，django在数据库中存放数据，将会默认为utc时间
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 告诉django静态文件在哪，在debug=True情况下生效，debug=False情况下失效
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

# 邮箱初始化送参数
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'jia2jiayuan@163.com'
EMAIL_HOST_PASSWORD = 'qq123456'
EMAIL_USE_TIL = False
EMAIL_FROM = 'jia2jiayuan@163.com'

# 设置文件上传路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # debug = False 时候，django进行静态文件代理
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 分页设置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10,
    'MARGIN_PAGES_DISPLAYED': 2,

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}



