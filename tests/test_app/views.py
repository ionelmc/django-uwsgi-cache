from django.core.cache import cache
from django.http import HttpResponse


def get(request, key):
    val = cache.get(key)
    print('test_app:get:%s => %s' % (key, val))
    return HttpResponse(val)


def set(request, key, value):
    cache.set(key, value)
    print('test_app:set:%s:%s' % (key, value))
    return HttpResponse("ok")


def clear(request):
    cache.clear()
    print('test_app:clear')
    return HttpResponse("ok")
