from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon/buy$', views.buy),
    url(r'^amadon/checkout$', views.checkout),
    url(r'^amadon/return$', views.back)
]