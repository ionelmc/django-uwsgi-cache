===============================
django-uwsgi-cache
===============================

| |docs| |travis| |appveyor| |coveralls| |landscape| |scrutinizer|
| |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/django-uwsgi-cache/badge/?style=flat
    :target: https://readthedocs.org/projects/django-uwsgi-cache
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/ionelmc/django-uwsgi-cache/master.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/django-uwsgi-cache

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/django-uwsgi-cache?branch=master
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/django-uwsgi-cache

.. |coveralls| image:: http://img.shields.io/coveralls/ionelmc/django-uwsgi-cache/master.png?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/django-uwsgi-cache

.. |landscape| image:: https://landscape.io/github/ionelmc/django-uwsgi-cache/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/django-uwsgi-cache/master
    :alt: Code Quality Status

.. |version| image:: http://img.shields.io/pypi/v/django-uwsgi-cache.png?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. |downloads| image:: http://img.shields.io/pypi/dm/django-uwsgi-cache.png?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. |wheel| image:: https://pypip.in/wheel/django-uwsgi-cache/badge.png?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. |supported-versions| image:: https://pypip.in/py_versions/django-uwsgi-cache/badge.png?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. |supported-implementations| image:: https://pypip.in/implementation/django-uwsgi-cache/badge.png?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/django-uwsgi-cache/master.png?style=flat
    :alt: Scrtinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/django-uwsgi-cache/

uWSGI Django cache backend.

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

* Django 1.4 or later

Settings
========

``UWSGI_CACHE_FALLBACK``

- ``False`` - raises Exception if ``uwsgi`` cannot be imported.
- ``True`` (default) - if uwsgi is not importable this cache backend will alias
  to LocMemCache. Note that south or other mangement commands might try to load
  the cache backend so this is why it's the default.
