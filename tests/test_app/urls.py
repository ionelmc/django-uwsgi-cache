try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from . import views


urlpatterns = [
    url('^get/(.*)', views.get),
    url('^set/(.*)/(.*)', views.set),
    url('^add/(.*)/(.*)', views.add),
    url('^clear', views.clear),
]

