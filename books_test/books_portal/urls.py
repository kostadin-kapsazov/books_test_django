from django.conf.urls import patterns, url

from .views import BooksView
from .views import DetailsView
from .views import AddView

urlpatterns = patterns('',
    url(r'^books/', BooksView.as_view(), name="books_portal_books"),
    url(r'^details/(?P<book_id>\d+)/$', DetailsView.as_view(), name="books_details"),
    url(r'^add/', AddView.as_view(), name="books_add"),
)
