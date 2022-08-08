import django_on_heroku
from decouple import config

from .base import *




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    # change
    'studybud-discord-clone.herokuapp.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #own
    'rooms.apps.RoomsConfig',
    'users.apps.UsersConfig',

    # reusable user app
    'userapp.apps.UserappConfig',

    # 3rd party
    'django_extensions',
]




DEBUG_PROPAGATE_EXCEPTIONS = True

# Heroku Logging

LOGGING = {
    'version': 1,
    'dissable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineo)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging-StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"






# django_on_heroku.settings(locals())
# django_on_heroku.settings(locals(), staticfiles=False)
# del DATABASES['default']['OPTIONS']['sslmode']
