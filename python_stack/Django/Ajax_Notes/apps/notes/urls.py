from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^change/(?P<id>\d+)$', views.change),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^all.html$', views.all_html)
]