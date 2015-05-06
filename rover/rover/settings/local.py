# Django settings for rover project.
import os

try:
    from rover.settings.base import *
except:
    pass


DEBUG = True
TEMPLATE_DEBUG = DEBUG
TIME_ZONE = None

DATABASES = {
             
    'default': {
       'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
       'NAME': os.path.join(BASE_DIR, 'rover.sqlite3'),                      # Or path to database file if using sqlite3.
        #'ENGINE' : 'django.db.backends.mysql',
        #'NAME': 'rover',
        # The following settings are not used with sqlite3:
        #'USER': 'root',
        #'PASSWORD': 'root',
        #'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        #'PORT': '3306',                      # Set to empty string for default.
    }
}



# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media-assets/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"

ADMIN_MEDIA_PREFIX = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static-assets')


# Make this unique, and don't share it with anybody.
SECRET_KEY = '6um84vppdfn$6y6+r1$g^c-myaa^m@v@t&bhs_g5knr#9^ovt1'


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'rover.wsgi_local.application'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
