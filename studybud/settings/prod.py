# import django_on_heroku
from decouple import config

from .base import *




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    # change
    # 'studybud-discord-clone.onrender.com',
    '*',
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

# AWS S3 settings

# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'


# AWS_S3_OBJECT_PARAMETERS = {
#    'CacheControl': 'max-age=86400'
# }


# AWS_LOCATION = 'static'


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]


# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'


# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'


# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'


# AWS_QUERYSTRING_AUTH = False

# AWS_HEADERS = {
#     'Access-Control-Allow-Origin': '*',
# }

# AWS_DEFAULT_ACL = 'public-read'













# DEBUG_PROPAGATE_EXCEPTIONS = True

# # Heroku Logging

# LOGGING = {
#     'version': 1,
#     'dissable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineo)s] %(message)s",
#             'datefmt': "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging-StreamHandler',
#         },
#     },
#     'loggers': {
#         'MYAPP': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     }
# }






# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# STATIC_ROOT = BASE_DIR / "staticfiles"

# STATIC_URL = '/static/'
# MEDIA_URL = '/static/images/'

# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]

# MEDIA_ROOT = BASE_DIR / 'static/images'

# django_on_heroku.settings(locals())
# django_on_heroku.settings(locals(), staticfiles=False)
# del DATABASES['default']['OPTIONS']['sslmode']
