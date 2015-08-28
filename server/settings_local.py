# -*- coding: utf-8 -*-
'''
Custom settins
Django settings for HyperKitty + Postorius
'''

import os
BASE_DIR = '/shared/mailman'
VAR_DIR = '/shared/mailman/var'

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, '.secret'), 'r') as secretFile:
    SECRET_KEY = secretFile.readline().strip(' \t\n\r')

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Mailman Admin', 'root@localhost'),
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['mail.sugarcub.org', 'localhost']
# And for BrowserID too, see
# http://django-browserid.rtfd.org/page/user/settings.html#django.conf.settings.BROWSERID_AUDIENCES
BROWSERID_AUDIENCES = ['http://mail.sugarcub.org', 'http://localhost', 'http://localhost:8000']

# Mailman API credentials
MAILMAN_REST_SERVER = MAILMAN_API_URL = 'http://localhost:8001'
MAILMAN_API_USER = MAILMAN_USER = 'restadmin'
MAILMAN_API_PASS = MAILMAN_PASS = 'restpass'
MAILMAN_ARCHIVER_KEY = 'SecretArchiverAPIKey'
MAILMAN_ARCHIVER_FROM = ('127.0.0.1', '::1', '::ffff:127.0.0.1')

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_DIR, 'mailman-web', 'mailman-web.sqlite'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'mailmanweb',
#         'USER': 'mailmanweb',
#         'PASSWORD': 'change-this-password',
#         'HOST': '127.0.0.1',
#         'PORT': '',
#     }
# }


# If you're behind a proxy, use the X-Forwarded-Host header
# See https://docs.djangoproject.com/en/1.5/ref/settings/#use-x-forwarded-host
USE_X_FORWARDED_HOST = True
# And if your proxy does your SSL encoding for you, set SECURE_PROXY_SSL_HEADER
# see https://docs.djangoproject.com/en/1.5/ref/settings/#secure-proxy-ssl-header
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/media/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: '/var/www/example.com/media/'
MEDIA_ROOT = os.path.join(VAR_DIR, 'mailman-web', 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' 'static/' subdirectories and in STATICFILES_DIRS.
# Example: '/var/www/example.com/static/'
STATIC_ROOT = os.path.join(VAR_DIR, 'mailman-web', 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            # 'class': 'logging.handlers.RotatingFileHandler',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(VAR_DIR, 'mailman-web', 'mailman-web.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': True,
        # },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'hyperkitty': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
}
