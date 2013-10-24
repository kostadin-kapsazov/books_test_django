from django.conf.urls import patterns, url

from .views import BooksView

urlpatterns = patterns('',
    url(r'^books/', BooksView.as_view(), name="books_portal_books"),
)
