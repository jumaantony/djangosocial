"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# heroku configuration
import django_heroku
import dj_database_url
from decouple import config

# cloudinary imports

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0n7s7#@i&ev3gjw!uw7&luy+3#o7r&#u6wod_ww-py2xhoj5hy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://socialdjango2.herokuapp.com', 'localhost', 'socialdjango2.herokuapp.com']
# Application definition

INSTALLED_APPS = [
    # created apps
    'account.apps.AccountConfig',
    'images.apps.ImagesConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'social.apps.django_app.default',

    # easy thumbnails
    'easy_thumbnails',

    # cloudinary
    'cloudinary',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# cloudinary config
cloudinary.config(
    cloud_name="kisumu-org",
    api_key="773424846215666",
    api_secret="SaMBazwZvkBe9vubaIMFgjzdR7M",
)

ROOT_URLCONF = 'bookmarks.urls'

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

WSGI_APPLICATION = 'bookmarks.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# authentication backends
AUTHENTICATION_BACKENDS = (
    # django authentication backends
    'django.contrib.auth.backends.ModelBackend',

    # email authentication
    'account.authentication.EmailAuthBackend',

    # Facebook Authentication
    'social_core.backends.facebook.FacebookOAuth2',

    # Twitter Auth
    'social_core.backends.twitter.TwitterOAuth',

    # GoogleOath2
    'social_core.backends.google.GoogleOAuth2',
)

SOCIAL_AUTH_FACEBOOK_KEY = '576032936717004'  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '031c31b600f7bf56b71e4ef3ef44892c'  # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = '4A5XqpGwDkbqGUWArPMpGMluN'  # Twitter API Key
SOCIAL_AUTH_TWITTER_SECRET = 'O5ctzVFD9acDna8QRCPEukVgqPvUrW7tbgnZrYHIDqXp1FacRb'  # Twitter API Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '96922575871-dj5j4d6sc6gh6p01h6pb55aq2u3nq4ts.apps.googleusercontent.com'  # google
# consumer key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'n1H4SgpIwqhy8h1dMOpuXTIU'  # google consumer secret Secret

# serving media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# absolute url overide for detaled user
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('user_detail',
                                        args=[u.username])
}

django_heroku.settings(locals())