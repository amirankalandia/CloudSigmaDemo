"""
Django settings for microbrewery project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b(7-%d)ux8c)+2th$*7wa^%lyl+m3i)56r^d5%0h%*a7ftt$uw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS = INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = ['django_prometheus']
LOCAL_APPS = ['beers']

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = 'microbrewery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'microbrewery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Retrieve the URL for backends
USER_BACKEND = os.environ['USER_BACKEND_URL']
WAREHOUSE_BACKEND = os.environ['WAREHOUSE_BACKEND_URL']

# Dear code reviewer.
# This is a demo project and that's why I have secrets exposed"

TOKENS_PUBLIC_KEY = '''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxF2uf9o4z4Wsg1sMHQeN
lSNoz09CV6psTgKOuUH5jyzzqP/Dd2WSfEzFu965dh1nT2Q8Pc+g8nu8y0Fbuh4z
dCDAHXJg629VYxTNQDjBXNsDeMB1x3APGGLCkTnNnm4AVL5c2/+ZqmpX52rmqV0c
VR8QJ7L2hsTsHsNPGtbx8UMLIX+hkocneqP33vxFk5hlLpIsERFtRXPDAWhF+/7A
amCRD3puUxE0P35eRt5kel3H6wXopwH9Jq6SS44NPu5EjuTR/Ne2oVYWfRUq1CP1
iKUI0u2y+aro9HRMqtNSASPxxDbcsadEhYqVB+7ak3X9qpTLM/dGy9vb8ZuizbwZ
KwIDAQAB
-----END PUBLIC KEY-----
'''

PUBLIC_KEY_PATH = '/opt/keys/public_key.pub'

if os.path.isfile(PUBLIC_KEY_PATH):
    with open(PUBLIC_KEY_PATH) as fp:
        TOKENS_PUBLIC_KEY = fp.read()
