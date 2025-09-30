"""
Django settings for test_project project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "+ln!mmswhbemdn@*v8sbic_n+i&j4+ct8(n=y09s81c)7fyyf2"  # noqa:S105

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = ("test_app",)

MIDDLEWARE_CLASSES = ()

ROOT_URLCONF = "test_app.urls"

WSGI_APPLICATION = "test_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = "/static/"

CACHES = {"default": {"BACKEND": "uwsgicache.UWSGICache", "LOCATION": "foobar"}}
UWSGI_CACHE_FALLBACK = os.getenv("UWSGI_CACHE_FALLBACK", False)
