'''
Django settings for sugarcub project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
'''

from django.conf.global_settings import AUTHENTICATION_BACKENDS, STATICFILES_FINDERS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

IS_PROD = os.getenv('DEPLOY_TYPE', 'dev') == 'prod'
DEBUG = not IS_PROD

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
    'sugarcub',
    'users',
    'bbbff',
    'agenda',

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
    'pipeline',

    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'core',  'templates'),
            os.path.join(BASE_DIR, 'admin', 'templates'),
            os.path.join(BASE_DIR, 'users', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'core.processors.custom_fields',
                'core.processors.mailing_list',
                'absolute.context_processors.absolute',
            ],
            'debug': False
        }
    },
]

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'admin',  'static'),
# )


ROOT_URLCONF = 'sugarcub.urls'

WSGI_APPLICATION = 'sugarcub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('SQL_DB', 'postgres'),
        'USER': os.getenv('SQL_USER', 'postgres'),
        'HOST': os.getenv('SQL_HOST', 'postgres'),
        'PORT': 5432,
    }
}

if os.getenv('SQL_PASSWORD'):
    DATABASES['default']['PASSWORD'] = os.getenv('SQL_PASSWORD')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'data', 'static')

STATICFILES_FINDERS = STATICFILES_FINDERS + [
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.ManifestFinder',
]
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
PIPELINE = {
    'PIPELINE_ENABLED': IS_PROD,
    'COMPILERS': ('pipeline.compilers.sass.SASSCompiler',),
    'STYLESHEETS': {
        'css': {
            'source_filenames': (
                'vendor/bootstrap/dist/css/bootstrap.min.css',
                'vendor/bootstrap-datepicker/dist/css/bootstrap-datepicker3.min.css',
                'vendor/cookieconsent2/build/dark-floating.css',
                'vendor/css-social-buttons/css/zocial.css',
                'vendor/font-awesome/css/font-awesome.min.css',
                'vendor/leaflet/dist/leaflet.css',
                'css/sugarcub.css',
                'css/sugarcub-admin.css',
                'css/bronycub.css',
            ),
            'output_filename': 'css/sugarcub.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'CSS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',

    'JAVASCRIPT': {
        'js': {
            'source_filenames': (
                'vendor/jquery/dist/jquery.min.js',
                'vendor/jquery-expander/jquery.expander.min.js',
                'vendor/bootstrap/dist/js/bootstrap.min.js',
                'vendor/bootstrap-datepicker/dist/js/bootstrap-datepicker.min.js',
                'vendor/bootstrap-datepicker/dist/locale/bootstrap-datepicker.fr.min.js',
                'vendor/cookieconsent2/build/cookieconsent.min.js',
                'vendor/leaflet/dist/leaflet.js',
                'js/dj.js',
                'js/expander.js',
                'js/konami.js',
            ),
            'output_filename': 'js/sugarcub.js',
        }
    },
    'JS_COMPRESSOR': 'pipeline.compressors.uglifyjs.UglifyJSCompressor',
}


# Media

MEDIA_URL  = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'data', 'media')


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True
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

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')

BROKER_URL            = 'redis://{}:6379/0'.format(REDIS_HOST)
CELERY_RESULT_BACKEND = 'redis://{}:6379/0'.format(REDIS_HOST)

CELERY_TASK_SERIALIZER   = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT    = ['json']
CELERY_TIMEZONE          = TIME_ZONE
CELERY_ENABLE_UTC        = True
CELERY_IMPORTS           = ('users.models', 'users.utils',)


# Cache

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://{}:6379/0'.format(REDIS_HOST),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
}


# Session

SESSION_ENGINE      = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'


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

if IS_PROD:
    from sugarcub.settings_prod import *
else:
    from sugarcub.settings_dev import *
    TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
