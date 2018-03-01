from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.books),
    url(r'^books/add$', views.add),
    url(r'^books/(?P<book_id>\d+)$', views.books_info),
    url(r'^books/create$', views.books_create),
    url(r'^reviews/create$', views.reviews_create),
    url(r'^reviews/delete/(?P<review_id>\d+)$', views.reviews_delete),
    url(r'^users/(?P<user_id>\d+)$', views.user_info),
]