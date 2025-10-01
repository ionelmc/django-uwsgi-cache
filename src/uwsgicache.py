"""uWSGI cache backend"""

import pickle

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache.backends.base import BaseCache
from django.core.cache.backends.base import InvalidCacheBackendError

try:
    import uwsgi
except ImportError as exc:
    if getattr(settings, "UWSGI_CACHE_FALLBACK", True):
        uwsgi = None
    else:
        raise InvalidCacheBackendError(
            "You're not running under uWSGI ! Set UWSGI_CACHE_FALLBACK=True in settings if you want to fallback to LocMemCache."
        ) from exc

__version__ = "1.0.1"
__all__ = ["UWSGICache"]

if uwsgi:

    class UWSGICache(BaseCache):
        pickle_protocol = pickle.HIGHEST_PROTOCOL

        def __init__(self, server, params):
            BaseCache.__init__(self, params)
            self._cache = uwsgi
            self._server = server

        def _exists(self, key):
            return self._cache.cache_exists(key, self._server)

        def add(self, key, value, timeout=True, version=None):
            key = self.make_and_validate_key(key, version=version)
            if self._exists(key):
                return False
            self._set(key, value, timeout)
            return True

        def get(self, key, default=None, version=None):
            key = self.make_and_validate_key(key, version=version)
            val = self._cache.cache_get(key, self._server)
            if val is None:
                return default
            return pickle.loads(val)  # noqa: S301

        def _set(self, key, value, timeout):
            if timeout is True or timeout == DEFAULT_TIMEOUT:
                timeout = self.default_timeout

            if timeout is None or timeout is False:
                # Django 1.6+: Explicitly passing in timeout=None will set a non-expiring timeout.
                uwsgi_timeout = 0
            elif timeout == 0:
                # Django 1.6+: Passing in timeout=0 will set-and-expire-immediately the value.
                uwsgi_timeout = -1
            else:
                uwsgi_timeout = timeout
            self._cache.cache_update(key, pickle.dumps(value, self.pickle_protocol), uwsgi_timeout, self._server)

        def set(self, key, value, timeout=True, version=None):
            key = self.make_and_validate_key(key, version=version)
            self._set(key, value, timeout)

        def delete(self, key, version=None):
            key = self.make_and_validate_key(key, version=version)
            self._cache.cache_del(key, self._server)

        def close(self, **kwargs):
            pass

        def clear(self):
            self._cache.cache_clear(self._server)
else:
    from django.core.cache.backends.locmem import LocMemCache as UWSGICache
