from django.core.cache import cache
from django.http import HttpResponse


def get(request, key):
    val = cache.get(key)
    print(f"test_app:get:{key} => {val}")
    return HttpResponse(val)


def set(request, key, value):
    timeout = request.GET.get("timeout", "default").lower()
    if timeout == "default":
        cache.set(key, value)
    elif timeout == "none":
        cache.set(key, value, timeout=None)
    else:
        cache.set(key, value, timeout=int(timeout))
    print(f"test_app:set:{key}:{value}:{timeout}")
    return HttpResponse("ok")


def add(request, key, value):
    timeout = request.GET.get("timeout", "default").lower()
    if timeout == "default":
        result = cache.add(key, value)
    elif timeout == "none":
        result = cache.add(key, value, timeout=None)
    else:
        result = cache.add(key, value, timeout=int(timeout))
    print(f"test_app:add:{key}:{value}:{timeout}")
    return HttpResponse(result)


def clear(request):
    cache.clear()
    print("test_app:clear")
    return HttpResponse("ok")
