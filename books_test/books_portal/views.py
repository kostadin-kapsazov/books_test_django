# coding: utf-8
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DetailView


from .models import Books


class BooksDetailView(DetailView):
    model = Books
    template_name = "books_portal/details.html"


class BooksCreateView(CreateView):
    model = Books
    template_name = "books_portal/add.html"
    success_url = reverse_lazy('books_portal')


class BooksUpdateView(UpdateView):
    model = Books
    template_name = "books_portal/add.html"
    success_url = reverse_lazy('books_portal')


class BooksListView(ListView):
    model = Books
    template_name = "books_portal/index.html"
