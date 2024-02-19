from .common import *

ALLOWED_HOSTS=['*']

DEBUG = True

INSTALLED_APPS = [
    'daphne',
    'drf_spectacular',
    'debug_toolbar',
]+INSTALLED_APPS

INTERNAL_IPS = [
    "0.0.0.0:8000",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '123@456',
        'HOST': 'db',
        'PORT': '5432',
    }
}