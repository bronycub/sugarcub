# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@93eg2!@%a4r@(qh9v#e2xpb@nkv^0=2em%9@k$_+qz9xr$&c@'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['sugarcub.loc']


# Mails

EMAIL_BACKEND      = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'contact@bronycub.org'
ADMINS             = [('Admin BronyCUB', 'bronycub@gmail.com')]
