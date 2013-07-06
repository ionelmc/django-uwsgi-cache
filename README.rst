===========================
    django-uwsgi-cache
===========================

Packaging of code from http://uwsgi-docs.readthedocs.org/en/latest/WebCaching.html with some small
changes.

Installation
============

``pip install django-uwsgi-cache`` and change settings to::

    CACHES = {
        'default': {
            'BACKEND': 'uwsgicache.UWSGICache',
        }
    }

Requirements
============

* Django 1.4 or later

Settings
========

``UWSGI_CACHE_FALLBACK``

- ``False`` - raises Exception if ``uwsgi`` cannot be imported.
- ``True`` (default) - if uwsgi is not importable this cache backend will alias
  to LocMemCache. Note that south or other mangement commands might try to load
  the cache backend so this is why it's the default.
