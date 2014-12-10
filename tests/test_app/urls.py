try:
    from django.conf.urls import patterns, handler404, handler500, include, url
except ImportError:
    from django.conf.urls.defaults import patterns, handler404, handler500, include, url

urlpatterns = patterns('test_app.views',
    url('^get/(.*)', 'get'),
    url('^set/(.*)/(.*)', 'set'),
    url('^add/(.*)/(.*)', 'add'),
    url('^clear', 'clear'),
)

