"""
Django settings for Project project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7!ojh#&gyu)3&$qjn#xc2g%m@ok6k&y6(x8=mf+0m-kvg)t2=+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dwitter',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'application',
        'USER':'root',
        'HOST':'localhost',
    'PASSWORD':'',
        'PORT':'3306',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'formatters': {
       'standard': {
           'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
           'datefmt' : "%d/%b/%Y %H:%M:%S"
       },
   },
   'handlers': {
       # 'null': {
       #     'level': 'DEBUG',
       #     'class': 'django.utils.log.NullHandler',
       # },
       'logfile': {
           'level': 'DEBUG',
           'class': 'logging.handlers.RotatingFileHandler',
           'filename': "dwitter.log",
           'maxBytes': 50000,
           'backupCount': 2,
           'formatter': 'standard',
       },
       'console':{
           'level':'INFO',
           'class':'logging.StreamHandler',
           'formatter': 'standard'
       },
   },
   'loggers': {
       'django': {
           'handlers':['console'],
           'propagate': True,
           'level': 'INFO',
       },
       'django.db.backends': {
           'handlers': ['console'],
           'level': 'DEBUG',
           'propagate': False,
       },
       'dwitter': {
           'handlers': ['console', 'logfile'],
           'level': 'DEBUG',
       },
   }
}

