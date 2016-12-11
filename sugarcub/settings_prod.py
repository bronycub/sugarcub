# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import random
import string


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
try:
    with open(os.path.join(BASE_DIR, '..', 'data', '.secret'), 'r') as secretFile:
        SECRET_KEY = secretFile.readline().strip(' \t\n\r')
except Exception:
    with open(os.path.join(BASE_DIR, '..', 'data', '.secret'), 'w') as secretFile:
        SECRET_KEY = ''.join((
            random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(64))
        )
        secretFile.write(SECRET_KEY)


ALLOWED_HOSTS  = os.getenv('ALLOWED_HOSTS', 'sugarcub.org,bronycub.org').split(',')


# Mails

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# TODO Allow for easy setup in BO
EMAIL_HOST           = os.getenv('HOST_IP', '172.17.42.1')
EMAIL_PORT           = 25
EMAIL_HOST_USER      = ''
EMAIL_HOST_PASSWORD  = ''
EMAIL_USE_TLS        = False
EMAIL_USE_SSL        = False
DEFAULT_FROM_EMAIL   = 'contact@' + ALLOWED_HOSTS[0]
EMAIL_SUBJECT_PREFIX = '[BronyCUB]'
ADMINS               = [('Admin BronyCUB', 'bronycub@gmail.com')]
