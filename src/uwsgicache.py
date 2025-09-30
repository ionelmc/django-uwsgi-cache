"""uWSGI cache backend"""

__version__ = "1.0.1"

try:
    from django.utils.encoding import force_bytes as stringify
except ImportError:
    from django.utils.encoding import smart_str as stringify
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache.backends.base import BaseCache
from django.core.cache.backends.base import InvalidCacheBackendError

try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    import uwsgi
except ImportError as exc:
    if getattr(settings, "UWSGI_CACHE_FALLBACK", True):
        uwsgi = None
    else:
        raise InvalidCacheBackendError(
            "You're not running under uWSGI ! Set UWSGI_CACHE_FALLBACK=True in settings if you want to fallback to LocMemCache."
        ) from exc

__all__ = ["UWSGICache"]

if uwsgi:

    class UWSGICache(BaseCache):
        pickle_protocol = pickle.HIGHEST_PROTOCOL

        def __init__(self, server, params):
            BaseCache.__init__(self, params)
            self._cache = uwsgi
            self._server = server

        def exists(self, key):
            return self._cache.cache_exists(stringify(key), self._server)

        def add(self, key, value, timeout=True, version=None):
            full_key = self.make_key(key, version=version)
            if self.exists(full_key):
                return False
            self._set(full_key, value, timeout)
            return True

        def get(self, key, default=None, version=None):
            full_key = self.make_key(key, version=version)
            val = self._cache.cache_get(stringify(full_key), self._server)
            if val is None:
                return default
            val = stringify(val)
            return pickle.loads(val)  # noqa: S301

        def _set(self, full_key, value, timeout):
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
            self._cache.cache_update(stringify(full_key), pickle.dumps(value, self.pickle_protocol), uwsgi_timeout, self._server)

        def set(self, key, value, timeout=True, version=None):
            full_key = self.make_key(key, version=version)
            self._set(full_key, value, timeout)

        def delete(self, key, version=None):
            full_key = self.make_key(key, version=version)
            self._cache.cache_del(stringify(full_key), self._server)

        def close(self, **kwargs):
            pass

        def clear(self):
            self._cache.cache_clear(self._server)
else:
    from django.core.cache.backends.locmem import LocMemCache as UWSGICache
