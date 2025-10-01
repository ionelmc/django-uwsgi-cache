import os

SECRET_KEY = "+ln!mmswhbemdn@*v8sbic_n+i&j4+ct8(n=y09s81c)7fyyf2"  # noqa:S105
DEBUG = TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
INSTALLED_APPS = ("test_app",)
ROOT_URLCONF = "test_app.urls"
WSGI_APPLICATION = "test_project.wsgi.application"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s.%(msecs)d] %(name)s (%(levelname)s) %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    },
    "loggers": {
        "django.request": {"level": "DEBUG"},
        "django.db.backends": {"level": "DEBUG"},
    },
    "filters": {},
}
CACHES = {"default": {"BACKEND": "uwsgicache.UWSGICache", "LOCATION": "foobar"}}
UWSGI_CACHE_FALLBACK = os.getenv("UWSGI_CACHE_FALLBACK", False)
