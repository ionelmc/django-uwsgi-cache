========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |github-actions| |coveralls| |codecov| |scrutinizer| |codacy| |codeclimate|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/django-uwsgi-cache/badge/?style=flat
    :target: https://readthedocs.org/projects/django-uwsgi-cache/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/ionelmc/django-uwsgi-cache/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/ionelmc/django-uwsgi-cache/actions

.. |coveralls| image:: https://coveralls.io/repos/github/ionelmc/django-uwsgi-cache/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://coveralls.io/github/ionelmc/django-uwsgi-cache?branch=main

.. |codecov| image:: https://codecov.io/gh/ionelmc/django-uwsgi-cache/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/ionelmc/django-uwsgi-cache

.. |codacy| image:: https://img.shields.io/codacy/grade/[Get ID from https://app.codacy.com/gh/ionelmc/django-uwsgi-cache/settings].svg
    :target: https://www.codacy.com/app/ionelmc/django-uwsgi-cache
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/ionelmc/django-uwsgi-cache/badges/gpa.svg
   :target: https://codeclimate.com/github/ionelmc/django-uwsgi-cache
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/django-uwsgi-cache.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/django-uwsgi-cache

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-uwsgi-cache.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/django-uwsgi-cache

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-uwsgi-cache.svg
    :alt: Supported versions
    :target: https://pypi.org/project/django-uwsgi-cache

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-uwsgi-cache.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/django-uwsgi-cache

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/django-uwsgi-cache/v1.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/django-uwsgi-cache/compare/v1.0.1...main


.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/ionelmc/django-uwsgi-cache/main.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/django-uwsgi-cache/


.. end-badges

uWSGI Django cache backend.

* Free software: BSD 2-Clause License

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
