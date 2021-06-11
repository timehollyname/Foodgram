from os import environ
from pathlib import Path

ENV = environ

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = ENV.get('SECRET_KEY')

DEBUG = int(ENV.get('DEBUG', 0))

ALLOWED_HOSTS = ENV.get('ALLOWED_HOSTS').split(' ')

INSTALLED_APPS = [
    'sorl.thumbnail',
    'rest_framework',
    'colorfield',
    'recipes',
    'users',
    'api',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'foodgram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.conf.conf',
                'context_processors.tags.tags',
                'context_processors.purchases.number_of_recipes_in_purchases',
            ],
        },
    },
]

WSGI_APPLICATION = 'foodgram.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': ENV.get('DB_ENGINE'),
        'NAME': ENV.get('DB_NAME'),
        'USER': ENV.get('POSTGRES_USER'),
        'PASSWORD': ENV.get('POSTGRES_PASSWORD'),
        'HOST': ENV.get('DB_HOST'),
        'PORT': int(ENV.get('DB_PORT')),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        ),
    },
]

LANGUAGE_CODE = ENV.get('LANGUAGE_CODE', 'en-us')

TIME_ZONE = ENV.get('TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'recipes:home'
LOGIN_URL = 'users:signin'
LOGOUT_REDIRECT_URL = 'recipes:home'
IF_NOT_FOUND_SESSION_THEN_REDIRECT_TO = 'recipes:home'

PASSWORD_RESET_TIMEOUT = 86400

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.PageNumberPagination'
    ),
    'PAGE_SIZE': 100
}

PAGINATION_RECIPES_SIZE = 9
PAGINATION_SUBSCRIPTIONS_SIZE = 9
RECIPES_IN_SUBSCRIPTIONS_SIZE = 3

EMAIL_HOST = ENV.get('EMAIL_HOST')
EMAIL_PORT = int(ENV.get('EMAIL_PORT', 465))
EMAIL_HOST_USER = ENV.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = ENV.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = int(ENV.get('EMAIL_USE_TLS', 0))
EMAIL_USE_SSL = int(ENV.get('EMAIL_USE_SSL', 0))
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

PURCHASES_SESSION_ID = 'purchases'

PROJECT_NAME = 'FoodGram'

SITE_ID = 1

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

    INTERNAL_IPS = ENV.get('INTERNAL_IPS').split(' ')

    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'
