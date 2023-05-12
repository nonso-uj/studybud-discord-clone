# import django_on_heroku
from decouple import config

from .base import *




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    # change
    'studybud-discord-clone.onrender.com',
    # '*',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'django_extensions',
    'storages',

    #own
    'rooms.apps.RoomsConfig',
    'users.apps.UsersConfig',

    # reusable user app
    'userapp.apps.UserappConfig',
]


STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# STATIC_URL = '/static/'
# MEDIA_URL = '/static/images/'

# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]

# MEDIA_ROOT = BASE_DIR / 'static/images'