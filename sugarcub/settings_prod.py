# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, '..', '..', '.secret'), 'r') as secretFile:
    SECRET_KEY = secretFile.readline().strip(' \t\n\r')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG          = False
TEMPLATE_DEBUG = False

with open(os.path.join(BASE_DIR, '..', '..', 'host'), 'r') as hostFile:
    HOST = hostFile.readline().strip('\t\n\r')
    ALLOWED_HOSTS  = HOST.split()


# Mails

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# TODO Allow for easy setup in BO
EMAIL_HOST          = '172.17.42.1'
EMAIL_PORT          = 25
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS       = False
EMAIL_USE_SSL       = False
DEFAULT_FROM_EMAIL  = 'contact@' + ALLOWED_HOSTS[0]
