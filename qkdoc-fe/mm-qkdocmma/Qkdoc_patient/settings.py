"""
Django settings for Qkdoc_patient project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

IMAGE_UPLOAD_FILE_TYPES = ['.jpeg', '.jpg', '.png']
IMAGE_UPLOAD_FILE_MAX_SIZE = 5*1000*1000

PATIENT_API_URL = os.environ.get('PATIENT_API_URL')
OTP_API_URL = os.environ.get('OTP_API_URL')

CITRUS_RETURN_URL = os.environ.get('CITRUS_RETURN_URL')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'juo%6kuidy#tji%nsvqi(x+qq=#@=%#(b^q7-c=04vcamkb@(5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'patientApp',
    'gunicorn',
	'django.contrib.humanize',
	'endless_pagination',
)

MIDDLEWARE_CLASSES = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
)

ROOT_URLCONF = 'Qkdoc_patient.urls'

WSGI_APPLICATION = 'Qkdoc_patient.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/pw_v3/'
STATIC_ROOT =''

STATICFILES_DIRS = (
                    BASE_DIR + '/static/pw_v3/',
)


TEMPLATE_DIRS = (BASE_DIR + '/templates/',)


# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': 'redis://[:'+os.environ.get('RQ_QUEUES_HOST')+':6379',
#         #'LOCATION' : 'redis://[:'+os.environ.get('RQ_QUEUES_PASSWORD')+']@'+os.environ.get('RQ_QUEUES_HOST')+':6379/0'
#     },
# }
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': os.environ.get('RQ_QUEUES_HOST')+':'+os.environ.get('RQ_QUEUES_PORT'),
    },
}
# Django Sessioin in Redis server
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_REDIS_HOST = os.environ.get('RQ_QUEUES_HOST')
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = os.environ.get('RQ_QUEUES_PASSWORD')
SESSION_REDIS_PREFIX = 'session'

DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE')
AWS_S3_SECURE_URLS = os.environ.get('AWS_S3_SECURE_URLS')     # use http instead of https
AWS_QUERYSTRING_AUTH = os.environ.get('AWS_QUERYSTRING_AUTH')     # don't add complex authentication-related query parameters for requests
AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID')     # enter your access key id
AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY') # enter your secret access key
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
S3_URL = os.environ.get('S3_URL')
#STATIC_URL = 'https://'+AWS_STORAGE_BUCKET_NAME+'.s3.amazonaws.com' + '/static/fe/'
STATIC_URL = S3_URL + 'static/pw_v3/'
#STATIC_ROOT = 'https://'+AWS_STORAGE_BUCKET_NAME+'.s3.amazonaws.com' + '/static/fe/'
STATIC_ROOT = S3_URL + 'static/pw_v3/'
STATICFILES_DIRS = (
                    BASE_DIR + '/static/pw_v3',
)

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


CITRUS_ACCESS_KEY = os.environ.get('CITRUS_ACCESS_KEY')
CITRUS_VANITY = os.environ.get('CITRUS_VANITY')

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

GENDER_TYPE = {'M': 'Male','F':'Female','O':'Other'}

ERROR_EMAIL_NOTIFIERS = os.environ.get('ERROR_EMAIL_NOTIFIERS')
if ERROR_EMAIL_NOTIFIERS:ERROR_EMAIL_NOTIFIERS = ERROR_EMAIL_NOTIFIERS.split(',')
else:ERROR_EMAIL_NOTIFIERS = ['sarath.sankar@in.theory-y.com', 'anvin.johnson@in.theory-y.com']    

INFO_EMAIL_NOTIFIERS = os.environ.get('INFO_EMAIL_NOTIFIERS')
if INFO_EMAIL_NOTIFIERS:INFO_EMAIL_NOTIFIERS = INFO_EMAIL_NOTIFIERS.split(',')
else:INFO_EMAIL_NOTIFIERS = ['ajil.jose@theory-y.com']    

QK_INFO_EMAIL_NOTIFIERS = os.environ.get('QK_INFO_EMAIL_NOTIFIERS')
if QK_INFO_EMAIL_NOTIFIERS:QK_INFO_EMAIL_NOTIFIERS = QK_INFO_EMAIL_NOTIFIERS.split(',')
else:QK_INFO_EMAIL_NOTIFIERS = ['support@qkdoc.com']


# for Amazon SES email sending
# email settings

AWS_S3_ACCESS_KEY_ID = ''
AWS_S3_SECRET_ACCESS_KEY = ''

EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

SERVER_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_REGION_NAME = os.environ.get('AWS_SES_REGION_NAME')
AWS_SES_REGION_ENDPOINT = os.environ.get('AWS_SES_REGION_ENDPOINT')
AWS_SES_AUTO_THROTTLE = None
AWS_SES_RETURN_PATH = os.environ.get('AWS_SES_RETURN_PATH')

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')


#Error Logging
ADMINS = (
  ('Sarath Sankar', 'sarath.sankar@in.theory-y.com'),
  ('Anvin Johnson', 'anvin.johnson@in.theory-y.com'),
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/nginx/qk-fe-debug.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'django_ses.SESBackend',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}



CITRUS_SERVICE_RETURN_URL = 'https://stag-fe.qkdoc.com/update-service-payment/'
MEDIA_URL = S3_URL
CITRUS_RETURN_URL = 'https://stag-fe.qkdoc.com/update-payment/'
