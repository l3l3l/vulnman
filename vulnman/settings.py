"""
Django settings for vulnman project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    from vulnman.secret_key import SECRET_KEY
except ImportError:
    from vulnman.utils.secret import generate_secret_key
    generate_secret_key(os.path.join(BASE_DIR, 'vulnman/secret_key.py'))
    from vulnman.secret_key import SECRET_KEY


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # keep before django.contrib.admin
    'dal',
    'dal_select2',
    'queryset_sequence',
    'dal_queryset_sequence',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'django_tex',
    'extra_views',
    'rest_framework',
    'account.apps.AccountConfig',
    'projects.apps.ProjectsConfig',
    'vulns.apps.VulnsConfig',
    'dashboard.apps.DashboardConfig',
    'credentials.apps.CredentialsConfig',
    'tools.apps.ToolsConfig'
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

ROOT_URLCONF = 'vulnman.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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
    {
        'NAME': 'tex',
        'BACKEND': 'django_tex.engine.TeXEngine',
        'APP_DIRS': True,
    },
]

WSGI_APPLICATION = 'vulnman.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

LOGIN_URL = "account:login"
LOGIN_REDIRECT_URL = "projects:project-list"
LOGOUT_REDIRECT_URL = "account:login"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = os.path.join(BASE_DIR, "static_files")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

LATEX_INTERPRETER = 'latexmk -pdf'

# for some reasons only works with os.path.join and not with pathlib
LATEX_GRAPHICSPATH = [
    os.path.join(BASE_DIR, "projects/templates/report/assets"),
    os.path.join(BASE_DIR, "uploads/proofs")
]

SEVERITY_COLORS = {
    'Critical': {'hex': '9c1720', 'chart_border': 'rgba(156, 23, 32, 1)', 'chart': 'rgba(156, 23, 32, 0.2)'},
    'High': {'hex': 'd13c0f', 'chart_border': 'rgba(209, 60, 15, 1)', 'chart': 'rgba(209, 60, 15, 0.2)'},
    'Medium': {'hex': 'e8971e', 'chart_border': 'rgba(232, 151, 30, 1)', 'chart': 'rgba(232, 151, 30, 0.2)'},
    'Low': {'hex': 'f5ee20', 'chart_border': 'rgba(245, 238, 32, 1)', 'chart': 'rgba(245, 238, 32, 0.2)'},
    'None': {'hex': '0acc2a', 'chart_border': 'rgba(10, 204, 42, 1)', 'chart': 'rgba(10, 204, 42, 0.2)'}
}

VULNMAN_CSS_THEME = "flatly"

EXTERNAL_TOOLS = {
    "nmap": "tools.parsers.nmap.NmapParser",
    "gobuster-vhost": "tools.parsers.gobuster.GobusterVhost"
}

try:
    from local_settings import *
except:
    pass
