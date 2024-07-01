"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import sys
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/operations/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "2_8dm8$#rp$nj^vfe28qpu^b8k1ew4bws_e&d+xn(jk116*rbz"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# strengthens the security of the Django application by preventing CSRF attacks via a secure cookie.
CSRF_COOKIE_SECURE = False

# strengthens application security by preventing attackers from intercepting user sessions via a secure cookie only.
SESSION_COOKIE_SECURE = False

# automatic redirection to HTTPS for all incoming connections
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ["1ldmind.com", "127.0.0.1", "51.75.16.153"]
CSRF_TRUSTED_ORIGINS = ['https://1ldmind.com']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "projets.apps.ProjetsConfig",
    "django_extensions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"

# Database configuration

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'base_ld',
        'USER': 'oasys',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation configuration

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization configuration

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images) configuration

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Collects static files for production
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'lionelmonthe184@gmail.com'
EMAIL_HOST_PASSWORD = 'snhdjcpwxttpingg'
DEFAULT_FROM_EMAIL = '1ldmind'

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

