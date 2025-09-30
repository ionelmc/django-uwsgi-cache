from django.urls import path

from . import views

urlpatterns = [
    path("get/<key>", views.get),
    path("set/<key>/<value>", views.set),
    path("add/<key>/<value>", views.add),
    path("clear", views.clear),
]
