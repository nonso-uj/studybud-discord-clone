from .base import *



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    # collectstatic in dev
    # "whitenoise.runserver_nostatic",

    'django.contrib.staticfiles',

    #own
    'rooms.apps.RoomsConfig',
    'users.apps.UsersConfig',

    # reusable user app
    'userapp.apps.UserappConfig',

    # 3rd party
    'django_extensions',
]


# Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.2/howto/static-files/


# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# STATIC_ROOT = BASE_DIR / "staticfiles"



STATIC_URL = '/static/'
MEDIA_URL = '/images/'


STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_ROOT = BASE_DIR / 'static/images'


# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
