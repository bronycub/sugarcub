"""
Django settings for sugarcub project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

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
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'multiform',
    'registration',
    'endless_pagination',
    'absolute',
)

DEV_DEPENDENCIES_APPS = (
)

INSTALLED_APPS = PROJECT_APPS + ('sugarcub',) + DEPENDENCIES_APPS

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

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'core.processors.custom_fields',
    'core.processors.humanitarian_actions',
    'core.processors.mailing_list',
    'django.core.context_processors.request',
    'absolute.context_processors.absolute',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'core',  'templates'),
    os.path.join(BASE_DIR, 'admin', 'templates'),
    os.path.join(BASE_DIR, 'users', 'templates'),
)


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'admin',  'static'),
)


ROOT_URLCONF = 'sugarcub.urls'

WSGI_APPLICATION = 'sugarcub.wsgi.application'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'unix:///shared/redis.sock',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True

USE_TZ = True


# Auth configuration

LOGIN_REDIRECT_URL      = '/'
LOGIN_URL               = '/login'
LOGOUT_URL              = '/logout'
ACCOUNT_ACTIVATION_DAYS = 7
AUTH_PROFILE_MODULE     = 'users.profile'


# Registration

REGISTRATION_AUTO_LOGIN = True


# Admin

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'


# Tests


# Per Collective Custom

from sugarcub.custom_settings import *

IS_PROD = os.getenv('DEPLOY_TYPE', 'dev') == 'prod'
if IS_PROD:
    from sugarcub.settings_prod import *
else:
    from sugarcub.settings_dev import *
