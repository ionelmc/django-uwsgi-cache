========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/django-uwsgi-cache/badge/?style=flat
    :target: https://readthedocs.org/projects/django-uwsgi-cache
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ionelmc/django-uwsgi-cache.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/django-uwsgi-cache

.. |requires| image:: https://requires.io/github/ionelmc/django-uwsgi-cache/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/django-uwsgi-cache/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/ionelmc/django-uwsgi-cache/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/django-uwsgi-cache

.. |codecov| image:: https://codecov.io/github/ionelmc/django-uwsgi-cache/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/django-uwsgi-cache

.. |landscape| image:: https://landscape.io/github/ionelmc/django-uwsgi-cache/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/django-uwsgi-cache/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg?style=flat
    :target: https://www.codacy.com/app/ionelmc/django-uwsgi-cache
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/ionelmc/django-uwsgi-cache/badges/gpa.svg
   :target: https://codeclimate.com/github/ionelmc/django-uwsgi-cache
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/django-uwsgi-cache.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. |downloads| image:: https://img.shields.io/pypi/dm/django-uwsgi-cache.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-uwsgi-cache.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-uwsgi-cache.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-uwsgi-cache.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/django-uwsgi-cache

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/django-uwsgi-cache/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/django-uwsgi-cache/


.. end-badges

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
