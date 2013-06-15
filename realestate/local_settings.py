# Django settings for realestate project.
#   THIS IS FOR LOCAL SERVER OVERRIDE ON ALL DEPLOYMENTS
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.abspath(os.path.dirname('manage.py'))
BASE_URL = "http://localhost/real-estate"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'real_estate',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'publicfunction',
        'PASSWORD': 'postgres',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

MEDIA_ROOT = PROJECT_PATH + '/media/'
MEDIA_URL = BASE_URL + '/media/'

#STATIC_ROOT = PROJECT_PATH + '/static/'
#STATIC_URL = BASE_URL + '/static/'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/'
)
