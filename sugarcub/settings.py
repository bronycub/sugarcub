'''
Django settings for sugarcub project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
'''

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS, AUTHENTICATION_BACKENDS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# Application definition

PROJECT_APPS = (
    'core',
    'users',
    'bbbff',
    'agenda',
)

DEPENDENCIES_APPS = (
    'stdimage',
    'bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admindocs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'multiform',
    'registration',
    'el_pagination',
    'absolute',
    'bootstrap3_datetime',
    'captcha',
    'ws4redis',
)

DEV_DEPENDENCIES_APPS = (
)

INSTALLED_APPS = ('sugarcub',) + DEPENDENCIES_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
)


# Templates

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + [
    'core.processors.custom_fields',
    'core.processors.mailing_list',
    'django.core.context_processors.request',
    'absolute.context_processors.absolute',
    'django.core.context_processors.static',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS
        },
    },
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'admin',  'static'),
]


ROOT_URLCONF = 'sugarcub.urls'

WSGI_APPLICATION = 'sugarcub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, '..', 'data', 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'data', 'static')


# Media

MEDIA_URL  = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'data', 'media')


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I20N = True
USE_L10N = True

USE_TZ = True


# Auth configuration

LOGIN_REDIRECT_URL       = '/'
LOGIN_URL                = '/login'
LOGOUT_URL               = '/logout'
ACCOUNT_ACTIVATION_DAYS  = 7
AUTH_PROFILE_MODULE      = 'users.profile'
AUTHENTICATION_BACKENDS += ('users.utils.EmailModelBackend', )


# Registration

REGISTRATION_AUTO_LOGIN = True


# Celery

BROKER_URL            = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

CELERY_TASK_SERIALIZER   = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT    = ['json']
CELERY_TIMEZONE          = TIME_ZONE
CELERY_ENABLE_UTC        = True
CELERY_IMPORTS           = ('users.models', 'users.utils',)


# Session

SESSION_ENGINE     = 'redis_sessions.session'
SESSION_REDIS_HOST = 'redis'


# Cache

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis:6379',
    },
}


# Admin

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'


# Bootstrap

BOOTSTRAP3 = {
    'horizontal_label_class': 'col-md-2',
    'horizontal_field_class': 'col-md-10'
}


# Sites Framework

SITE_ID = 1


# Tests


# Per Collective Custom

from sugarcub.custom_settings import *

IS_PROD = os.getenv('DEPLOY_TYPE', 'dev') == 'prod'
if IS_PROD:
    from sugarcub.settings_prod import *
else:
    from sugarcub.settings_dev import *
