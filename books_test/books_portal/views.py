# coding: utf-8


from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404

from .models import BooksForm
from .models import Books


class BooksView(TemplateView):
    template_name = "books_portal/index.html"

    def get_context_data(self, **kwargs):
        context = super(BooksView, self).get_context_data(**kwargs)
        books_list = list(Books.objects.all())
        context.update({
            'books_list': books_list,
        })

        return context


class AddView(TemplateView):
    template_name = "books_portal/add.html"

    def post(self, request, *args, **kwargs):
        f = BooksForm(request.POST)
        f.save()

        return HttpResponseRedirect(reverse('books_portal_books'))


class DetailsView(TemplateView):
    template_name = "books_portal/details.html"

    def get_context_data(self, **kwargs):
        context = super(DetailsView, self).get_context_data(**kwargs)

        book_id = kwargs.get('book_id')

        result = list(Books.objects.filter(id=book_id))

        if result:
            book = result[0]
        else:
            raise Http404()

        context.update({
            'book': book,
        })

        return context