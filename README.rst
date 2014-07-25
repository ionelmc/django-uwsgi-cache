===============================
django-uwsgi-cache
===============================

.. image:: http://img.shields.io/travis/ionelmc/django-uwsgi-cache/master.png
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/django-uwsgi-cache

.. image:: http://img.shields.io/coveralls/ionelmc/django-uwsgi-cache/master.png
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/django-uwsgi-cache

.. image:: http://img.shields.io/pypi/v/django-uwsgi-cache.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. image:: http://img.shields.io/pypi/dm/django-uwsgi-cache.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

uWSGI Django cache backend. Origianlly taken from http://uwsgi-docs.readthedocs.org/en/latest/WebCaching.html

* Free software: BSD license

Installation
============

``pip install django-uwsgi-cache`` and change settings to::

    CACHES = {
        'default': {
            'BACKEND': 'uwsgicache.UWSGICache',

            # and optionally, if you use a different cache name
            'LOCATION': 'foobar'
        }
    }

Requirements
============

* Django 1.3 or later

Settings
========

``UWSGI_CACHE_FALLBACK``

- ``False`` - raises Exception if ``uwsgi`` cannot be imported.
- ``True`` (default) - if uwsgi is not importable this cache backend will alias
  to LocMemCache. Note that south or other mangement commands might try to load
  the cache backend so this is why it's the default.
