"""
Django settings for djmatch project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from os.path import join, dirname
from dotenv import load_dotenv
from .finders import MyStaticFilesConfig
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SITE_URL = "djmatch.herokuapp.com"
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k5@(so71g$m^1bdq8sx55tm74q30d9rpojdoyx^qov1h#^iq2l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'djmatch.finders.MyStaticFilesConfig',
    'cuser',
    'project',
    'user',
    'uclapi',
    'crispy_forms',
    'django_filters',
    'django_select2',
    'storages',
    'pipeline',
    'social_widgets',
    'django_nose_qunit',
    'django_cron'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'djmatch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djmatch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djmatch',
        'USER': 'djmatch',
        'PASSWORD': 'Qazwsx12@',
        'HOST': '127.0.0.1',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_89c0b34174e3d16',
        'USER': 'b78e5634f17644',
        'PASSWORD': '7a57fde5',
        'HOST': 'us-cdbr-iron-east-05.cleardb.net',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
'''
SELECT2_CSS = 'project/css/select2.css'
SELECT2_JS = 'project/js/select2ff.js'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
        "TIMEOUT" : 300000,

    }
}

AUTH_USER_MODEL = 'cuser.CUser'
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]





# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/build/'
# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_PLUGINS = [
    'django_nose_qunit.QUnitPlugin'
]
NOSE_ARGS = [
    '--with-django-qunit',
    '--nologcapture'
]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'contact.dataspartan@gmail.com'
EMAIL_HOST_PASSWORD = 'dataspartan123'
EMAIL_PORT = 587
LOGIN_REDIRECT_URL = '/project'
LOGGING = {
 'version': 1,
 'disable_existing_loggers': False,
 'filters': {
 'require_debug_false': {
 '()': 'django.utils.log.RequireDebugFalse'
 }
 },
 'handlers': {
 'logfile': {
 'class': 'logging.handlers.WatchedFileHandler',
 'filename': 'D:\home\site\wwwroot\myapp.log'
 }
 },
 'loggers': {
 'django': {
 'handlers': ['logfile'],
 'level': 'ERROR',
 'propagate': False,
 }
 }
 }

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
SESSION_ENGINE  = "django.contrib.sessions.backends.cached_db"

AWS_ACCESS_KEY_ID = 'AKIAIKKLZZHMF7NXV5GA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'notice-board-static'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'djmatch.storage_backends.MediaStorage'


PIPELINE = {
    'PIPELINE_ENABLED' : False,
    'CSS_COMPRESSOR':'pipeline.compressors.cssmin.CSSMinCompressor',
    'CSSMIN_BINARY': 'cssmin',
    'JS_COMPRESSOR' : 'pipeline.compressors.jsmin.JSMinCompressor',
    'STYLESHEETS': {
            'my_app': {
                'source_filenames': (
                    'project/css/bootstrap.min.css',
                    'project/css/font-awesome.min.css',
                    'project/css/ladda-themeless.min.css',
                    'project/css/panel.css',
                    'project/toastr.min.css',
                    'project/css/select2.css',
                    'project/css/index.css'
                ),
                'output_filename': 'compress/css/final.min.css',
            },
    },
    'JAVASCRIPT': {
        'layout': {
            'source_filenames': (
                'project/js/bootstrap.min.js',
                'project/js/toastr.min.js',
                'project/js/jquery.validation.js',
                'project/js/spin.min.js',
                'project/js/ladda.min.js',
                'project/js/layout.js',
                'project/js/file.js'

            ),
            'output_filename': 'compress/js/layout.min.js',
        },
        'create' : {
            'source_filenames' : (
                'project/js/jquery.min.js',
                'project/js/bootstrap.min.js',
                'project/js/compress.min.js',
                'project/js/select2.js',
                'project/js/django_select2.js',
                'project/js/index.js'
            ),
            'output_filename' : 'compress/js/create.min.js'
        },
        'detail' : {
             'source_filenames' : (
                 'project/js/select2.js',
                 'project/js/filter_django_select2.js',
                 'project/js/recommendations.js',
                 'project/js/panel.js',
                 'project/js/detail.js',
             ),
             'output_filename' : 'compress/js/detail.min.js'
        },
        'index' : {
             'source_filenames' : (
                 'project/js/select2.js',
                 'project/js/recommendations.js',
                 'project/js/filter_django_select2.js',
                 'project/js/panel.js',
             ),
             'output_filename' : 'compress/js/index.min.js'
        }
    }
}

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static/build')

CRON_CLASSES = [
    "djmatch.cron.MyCronJob",
    # ...
]
