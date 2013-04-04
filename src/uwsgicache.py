"""uWSGI cache backend"""

from django.core.cache.backends.base import BaseCache, InvalidCacheBackendError
from django.utils.encoding import smart_str
from django.conf import settings

try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    import uwsgi
except:
    if getattr(settings, "UWSGI_CACHE_FALLBACK", True):
        uwsgi = None
    else:
        raise InvalidCacheBackendError(
            "You're not running under uWSGI ! "
            "Set UWSGI_CACHE_FALLBACK=True in settings if you want to fallback "
            "to LocMemCache."
        )

if uwsgi:
    class UWSGICache(BaseCache):
        def __init__(self, server, params):
            BaseCache.__init__(self, params)
            self._cache = uwsgi
            self._server = server

        def exists(self, key):
            return self._cache.cache_exists(smart_str(key), self._server)

        def add(self, key, value, timeout=0):
            if self.exists(key):
                return False
            return self.set(key, value, timeout, self._server)

        def get(self, key, default=None):
            val = self._cache.cache_get(smart_str(key), self._server)
            if val is None:
                return default
            val = smart_str(val)
            return pickle.loads(val)

        def set(self, key, value, timeout=0):
            self._cache.cache_update(smart_str(key), pickle.dumps(value), timeout, self._server)

        def delete(self, key):
            self._cache.cache_del(smart_str(key), self._server)

        def close(self, **kwargs):
            pass

        def clear(self):
            pass
else:
    from django.core.cache.backends.locmem import LocMemCache as UWSGICache
    from django.core.cache.backends import locmem

class CacheClass(UWSGICache):
    pass
