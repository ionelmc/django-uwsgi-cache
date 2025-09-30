Changelog
=========

1.1.0 (2025-10-01)
------------------

* Fixed bug that occurs when timeout=DEFAULT_TIMEOUT is used.
  Contributed by György Kiss in `#12 <https://github.com/ionelmc/django-uwsgi-cache/pull/12>`_.
* Added pickle_protocol class property (defaults to ``pickle.HIGHEST_PROTOCOL``).
* Django 4.2 or later is required now.
* Python 3.9 or later is required now.

1.0.1 (2015-07-01)
------------------

* Stop depending explicitly on ``uwsgi`` in ``setup.py`` (helps with development and such).

1.0.0 (2014-12-10)
------------------

* Support for special timeout values in Django 1.6 and 1.7 (contributed by Laurent Payot)

0.3.0 (2014-07-25)
------------------

* Python 3 support (contributed by Laurent Payot)
* Support for ``cache.clear`` (contributed by Omer Katz)

0.? (?)
-------

* N/A (contributed by Riccardo Magliocchetti)
