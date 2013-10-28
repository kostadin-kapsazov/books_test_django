from django.conf.urls import patterns, url

from .views import BooksDetailView
from .views import BooksCreateView
from .views import BooksUpdateView
from .views import BooksListView

urlpatterns = patterns('',
    url(r'^books/$', BooksListView.as_view(), name="books_portal"),
    url(r'^books/(?P<pk>\d+)/view/$', BooksDetailView.as_view(), name="books_details"),
    url(r'^books/add/$', BooksCreateView.as_view(), name="books_add"),
    url(r'^books/(?P<pk>\d+)/edit/$', BooksUpdateView.as_view(), name="books_edit"),
)
