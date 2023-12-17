# -*- coding: utf-8 -*-

# django-debug-toolbar
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

"""
Django settings for practice_django project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # --======= installed packages =======--
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#installation
    'debug_toolbar',
    # https://channels.readthedocs.io/en/latest/installation.html#installation
    # 'channels', commented out temporarily
    # https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/#module-django.contrib.humanize
    'django.contrib.humanize',
    # --=== allauth ===--
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    # # --End allauth --
    'crispy_forms',
    'crispy_bootstrap5',
    'ckeditor',
    # --======= project applications =======--
    'blog.apps.BlogConfig',
    # --======= installed packages =======--
    # Add django_cleanup to the bottom of INSTALLED_APPS
    # https://github.com/un1t/django-cleanup/#configuration
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django-debug-toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # Add the account middleware:
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'practice_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# --======= django-allauth =======--
# https://docs.allauth.org/en/latest/installation/quickstart.html#quickstart
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },
    'github': {
        "SCOPE": [
            "user",
            "repo",
            "read:org",
        ],
    }
}
# -- End django-allauth --

WSGI_APPLICATION = 'practice_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_practice_django_1.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# https://docs.djangoproject.com/en/4.2/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


STATICFILES_DIRS = [
    # "/home/special.polls.com/polls/static",
]


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --======== django-crispy-forms =======--
# https://django-crispy-forms.readthedocs.io/en/latest/install.html
# CRISPY_TEMPLATE_PACK = 'uni_form'

# https://github.com/django-crispy-forms/crispy-bootstrap5#usage
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
# -- End django-crispy-forms --


# --======= django-ckeditor =======--
# https://github.com/django-ckeditor/django-ckeditor#optional---customizing-ckeditor-editor
CKEDITOR_CONFIGS = {
    'default': {
        'width': 'auto',
    }
}
# -- End django-ckeditor --

# channels
# https://channels.readthedocs.io/en/latest/installation.html#installation
"""
ASGI_APPLICATION = "practice_django.routing.application"

# https://channels.readthedocs.io/en/latest/topics/channel_layers.html?highlight=inmemorychannellayer#in-memory-channel-layer
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
"""
# End channels
