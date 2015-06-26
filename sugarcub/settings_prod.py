# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''  # TODO get from local install (not versioned)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG          = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS  = []  # TODO Allow for easy setup in BO


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'database', 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')


# Media

MEDIA_URL  = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')


# Mails

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# TODO Allow for easy setup in BO
EMAIL_HOST          = ''
EMAIL_PORT          = ''
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS       = ''
EMAIL_USE_SSL       = ''


# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
