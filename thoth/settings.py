"""
Django settings for thoth project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8!i#^l@g*o&q9zm2-o==$q+agbl^^k&$6pn780jt)v%vmou(3-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'authtools',
    'guardian',
    'djrill',
    'bootstrap3',
    'scribe',
    'accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'thoth.urls'

WSGI_APPLICATION = 'thoth.wsgi.application'

AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
)

ANONYMOUS_USER_ID = -1

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'

# Template Directories
TEMPLATE_DIRS = (
        (os.path.join(PROJECT_PATH, 'templates'),)
)

# Web Domain
WEB_URL = 'http://127.0.0.1:8000'

# Static
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles' 
STATICFILES_DIRS = (
    ('', os.path.join(PROJECT_PATH, 'static')),
)

# Media
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

# Heroku
# Parse database configuration from $DATABASE_URL
import dj_database_url
import os
if os.getcwd() == "/app":
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    WEB_URL = 'http://secure-thicket-4638.herokuapp.com'
    DEFAULT_FROM_EMAIL = 'app21424083@heroku.com'
    MANDRILL_API_KEY = "d2HU9QVfRIiIamNvr0AbVA"
    EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
